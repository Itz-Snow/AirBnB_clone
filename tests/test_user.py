#!/usr/bin/python3

""" import unittest, user class """
import unittest
from models.user import User
import re

class TestUserInfo(unittest.TestCase):
    """ Test user class """
    def setUp(self):
        """ create user instance """
        self.new_user = User()

    def test_firstname(self):
        """ test the information provided in firstname """
        self.assertEqual(type(self.new_user.first_name), str)

    def test_email(self):
        """ test email address """
        self.assertEqual(type(self.new_user.email), str)

    def test_lastname(self):
        """ test type of last name """
        self.assertEqual(type(self.new_user.last_name), str)

    def test_password(self):
        """ test password """
        self.assertEqual(type(self.new_user.password), str)