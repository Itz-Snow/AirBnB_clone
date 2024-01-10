#!/usr/bin/python3
"""This module defines all common attributes/methods for other HBnB classes"""

from uuid import uuid4
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """A base class for all hbnb models"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class."""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key in ["created_at", "updated_at"]:
                        setattr(
                            self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                        )
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the instance"""
        class_name = self.__class__.__name__
        return f"[{class_name}] ({self.id}) {self.__dict__}"

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Convert instance into dict format"""
        result_dict = self.__dict__.copy()
        result_dict["created_at"] = self.created_at.isoformat()
        result_dict["updated_at"] = self.updated_at.isoformat()
        result_dict["__class__"] = self.__class__.__name__
        return result_dict
