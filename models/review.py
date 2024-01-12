#!/usr/bin/python3
"""This module defines the Review class."""
from models.base_model import BaseModel

class Review(BaseModel):
    """A class for representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
