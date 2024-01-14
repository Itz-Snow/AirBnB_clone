#!/usr/bin/python3

""" import unittest """
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """ test state """

    def test_name(self) -> None:
        """ test name attribute """
        my_state = State()
        self.assertEqual(type(my_state.name), str)