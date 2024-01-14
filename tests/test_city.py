#!/usr/bin/python3

""" import unittest """
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """ test city class """

    def setUp(self) -> None:
        """ create instance """
        self.my_city = City()

    def test_stateid(self) -> None:
        """ test state_id """
        self.assertEqual(type(self.my_city.state_id), str)

    def test_name(self) -> None:
        """ test name attribute """
        self.assertEqual(type(self.my_city.name), str)