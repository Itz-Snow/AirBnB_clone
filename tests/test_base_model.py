#!/usr/bin/python3

""" import statement for other files """

import unittest
from models.base_model import BaseModel as base
from models.engine.file_storage import FileStorage as file
import datetime
import tempfile


class TestBaseModel(unittest.TestCase):
    """ Test cases for BaseModel """
    def setUp(self) -> None:
        self.b = base()

    def test_args_init(self):
        """ test init """
        self.assertEqual(type(base()), base)

    def test_args_withaRG(self):
        """ TEST base() with arguent"""
    def test_print(self):
        self.assertEqual(type(self.b.__str__()), str)

    def test_to_dict(self):
        """ test to_dict method """
        self.assertTrue(type(self.b.to_dict() == dict))

    def test_save(self) -> None:
        """ test base_model save's method """
        another_b = base()
        old_updated_at = another_b.updated_at
        another_b.save()
        new_updated_at = another_b.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)
        self.assertEqual(type(self.b.updated_at), datetime.datetime)



class TestStorage(unittest.TestCase):
    """ Testing the storage class """
    def setUp(self):
        """ test setup for instantiation"""
        self.storage = file()

    def test_all(self):
        self.assertIs(type(self.storage.all()), dict)

    def test_file_paths(self):
        self.assertEqual(str, type(self.storage._FileStorage__file_path))
        # data = self.storage._FileStorage__file_path.split(".")
        # with self.assertRaises(TypeError):
        #     self.assertEqual(data[-1], "json")


    def test_new(self):
        self.assertTrue(type(self.storage._FileStorage__objects), dict)

    def test_objects(self):
        self.assertTrue(type(self.storage._FileStorage__objects), dict)

    def test_save(self):
        with self.assertRaises(FileNotFoundError):
            with open("te.txt") as fq:
                self.storage.save(self)

    def test_reload(self):
        with self.assertRaises(FileNotFoundError):
            with open("te.json") as fq:
                self.storage.reload(self)