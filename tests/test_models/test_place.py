#!/usr/bin/python3

"""
Testing outputs for BaseModel
"""

from models.base_model import BaseModel


class TestPlaceClass(unittest.TestCase):
    """
    Test Place class unittesting
    """

    def instance_creation(self):
        """
        Create instance of Class Place
        """
        self.place = Place()