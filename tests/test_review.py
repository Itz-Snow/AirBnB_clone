#!/usr/bin/python3

""" import unittest """
import unittest
from models.review import Review


class TestReviewClass(unittest.TestCase):
    """ Test review class """

    def setUp(self) -> None:
        """ create Review class """
        self.review = Review()

    def test_place_id(self) -> None:
        """ test place_id """
        self.assertEqual(type(self.review.place_id), str)

    def test_userId(self) -> None:
        """ test user_id """
        self.assertEqual(type(self.review.user_id), str)

    def test_text(self) -> None:
        """ test text """
        self.assertEqual(type(self.review.text), str)