#!/usr/bin/python3

""" import unitttest """
import unittest
from models.place import Place


class TestPlaceClass(unittest.TestCase):
    """ class for testing place.py in models directory """

    def setUp(self) -> None:
        """ create instances of Place """
        self.my_place = Place()

    def test_cityID(self) -> None:
        """ tests city_id attribute """
        self.assertEqual(type(self.my_place.city_id), str)

    def test_userId(self) -> None:
        """ tests user_id """
        self.assertEqual(type(self.my_place.user_id), str)

    def test_name(self) -> None:
        """ tests name """
        self.assertTrue(type(self.my_place.name) == str)

    def test_description(self) -> None:
        """ tests description attribute of my_place """
        self.assertTrue(type(self.my_place.description) == str)

    def test_numberRooms(self) -> None:
        """ tests the number of rooms attribute(number_rooms) """
        self.assertTrue(type(self.my_place.number_rooms) == int)

    def test_numberBath(self) -> None:
        """ tests the number of bathrooms """
        self.assertTrue(type(self.my_place.number_bathrooms) == int)

    def test_maxGuest(self) -> None:
        """ test to make sure number of guests in an int """
        self.assertTrue(type(self.my_place.max_guest) == int)

    def test_nightprice(self) -> None:
        """ test the prince_by_night attr """
        self.assertTrue(type(self.my_place.price_by_night) == int)

    def test_latitide(self) -> None:
        """ test latitude """
        self.assertTrue(type(self.my_place.latitude) == float)

    def test_longitude(self) -> None:
        """ test longitude """
        self.assertTrue(type(self.my_place.longitude) == float)

    def test_amenityid(self) -> None:
        """ test amenity_ids """
        self.assertTrue(type(self.my_place.amenity_ids) == list)

    def test_amenityid(self) -> None:
        self.assertTrue(all(isinstance(i, str) for i
                        in self.my_place.amenity_ids))