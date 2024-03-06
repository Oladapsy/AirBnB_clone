#!/usr/bin/python3
"""
    A class that test thee Base model
    to ensure it is working properly
    using unit test
    """
from models.base_model import BaseModel
import unittest
from datetime import datetime
from datetime import timedelta
from time import sleep


class TestBaseModel_instantation(unittest.TestCase):
    """ used to test the base model"""
    def test_no_args_instance(self):
        """ check if the model has no args """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_if_id_is_string(self):
        """ test if id is a string"""
        Bm1 = BaseModel()
        Bid = Bm1.id
        self.assertEqual(str, type(Bid))

    def test_if_id_is_not_others(self):
        """ test if id is not a string"""
        Bm1 = BaseModel()
        Bid = Bm1.id
        self.assertNotEqual(int, type(Bid))
        self.assertNotEqual(float, type(Bid))
        self.assertNotEqual(list, type(Bid))
        self.assertNotEqual(dict, type(Bid))
        self.assertNotEqual(dict, type(Bid))
        self.assertNotEqual(set, type(Bid))

    def test_two_models_id(self):
        """test if two object ids are not equal as we don't want it to"""
        Bm1 = BaseModel()
        Bm2 = BaseModel()
        self.assertNotEqual(Bm1, Bm2)

    def test_created_at(self):
        """ let us check if current date is a datetime type"""
        Bm1 = BaseModel()
        time = Bm1.created_at
        self.assertEqual(datetime, type(time))

    def test_updated_at(self):
        """ let us check if updated_at date is a datetime type"""
        Bm1 = BaseModel()
        time = Bm1.updated_at
        self.assertEqual(datetime, type(time))

    def test_created_at_test_future_time(self):
        """ let us check if current date is assigned"""
        Bm1 = BaseModel()
        time = Bm1.created_at
        self.assertNotEqual(type(time), timedelta(days=1))

    def test_created_at_is_less_than_update_at(self):
        """check if time created is less than time updated"""
        Bm1 = BaseModel()
        time = Bm1.created_at
        Bm1.save()
        time2 = Bm1.updated_at
        self.assertLess(time, time2)

    def test_created_at_is_less_than_new_created_at(self):
        """check if time created is less than time the second class
        object is created
        """
        Bm1 = BaseModel()
        time = Bm1.created_at
        sleep(1)
        Bm2 = BaseModel()
        time2 = Bm2.created_at
        self.assertLess(time, time2)

    def test_updated_of_two_base_class(self):
        """ check if two classes updated at are different"""
        Bm1 = BaseModel()
        sleep(1)
        Bm2 = BaseModel()
        self.assertLess(Bm1.updated_at, Bm2.updated_at)

    def test_str_rep(self):
        """ test the string representation"""
        dt = datetime.now()
        Bm1 = BaseModel()
        Bm1.id = "23456"
        Bm1.number = 1997
        Bm1.name = "My first Model"
        Bm1.created_at = dt
        Bm1.updated_at = dt
        Bm1str = Bm1.__str__()
        self.assertIn("[BaseModel] (23456)", Bm1str)
        self.assertIn("'id': '23456'", Bm1str)
        self.assertIn("'number': 1997", Bm1str)
        self.assertIn("'name': 'My first Model'", Bm1str)
        self.assertIn("'updated_at': " + datetime.now()), Bm1str)


if __name__ == "__main__":
    unittest.main()
