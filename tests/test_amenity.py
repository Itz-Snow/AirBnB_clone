#!/usr/bin/python3

""" import unittest """
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ test amenity class """

    def test_name(self) -> None:
        """ test name attribute """
        the_amenity = Amenity()
        self.assertEqual(type(the_amenity.name), str)