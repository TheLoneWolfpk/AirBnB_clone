#!/usr/bin/python3
"""
<<<<<<< HEAD
unittest to test the City class
"""

import unittest
import models
import os
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from models.engine.file_storage import FileStorage
import uuid


class TestCity(unittest.TestCase):
    """
    Class to test the BaseModel Function
    """

    def test_init_no_args(self):
        # Testing initialization with args
        self.assertEqual(City, type(City()))

    def test_public_id(self):
        # checks if id is public
        self.assertEqual(str, type(City().id))

    def test_name_types(self):
        state = City()
        self.assertIs(type(state.name), str)

    def test_public_created_at_datetime(self):
        # checks if created datetime is public
        self.assertEqual(datetime, type(City().created_at))

    def test_updated_at_datetime(self):
        # checks if updated datetime is public
        self.assertEqual(datetime, type(City().updated_at))

    def test_unused_args(self):
        obj = City(None)
        self.assertNotIn(None, obj.__dict__.values())

    def test_init_with_kwargs(self):
        # Testing City initialization with kwargs
        d_time = datetime.now()
        d_time_i =d_time.isoformat()
        state1 = City(id="861", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(state1.id, "861")
        self.assertEqual(state1.created_at, d_time)
        self.assertEqual(state1.updated_at, d_time)

    def test_init_without_kwargs(self):
        # Testing initialization without kwargs
        obj = City()
        self.assertTrue(hasattr(obj, 'id'))
        self.assertIsInstance(obj.id, str)
        self.assertTrue(hasattr(obj, 'created_at'))
        self.assertIsInstance(obj.created_at, datetime)
        self.assertTrue(hasattr(obj, 'updated_at'))
        self.assertIsInstance(obj.updated_at, datetime)

    def test_inst_with_None_kwargs(self):
        # test none kwargs
        with self.assertRaises(TypeError):
            City(id=None, created_at=None, updated_at=None)

    def test_two_unique_ids(self):
        # Tests if two ids are unique
        obj1 = City()
        obj2 = City()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_to_dict_method(self):
        # Testing the __dict__ method
        obj = City()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertEqual(obj_dict['__class__'], 'City')
        self.assertEqual(obj_dict['id'], obj.id)
        self.assertEqual(obj_dict['created_at'], obj.created_at.isoformat())
        self.assertEqual(obj_dict['updated_at'], obj.updated_at.isoformat())

    def test_dict_type(self):
        # test the type of to_dict
        obj = City()
        self.assertTrue(dict, type(obj.to_dict))

    def test_state_id(self):
        city = City()
        self.assertIs(type(city.state_id), str)

    def test_dict_correct(self):
        # test to check the correctness of the keys
        obj = City()
        self.assertIn("id", obj.to_dict())
        self.assertIn("created_at", obj.to_dict())
        self.assertIn("updated_at", obj.to_dict())
        self.assertIn("__class__", obj.to_dict())

    def test_dict_add_attributes(self):
        # test to check on additino of attributes to dict
        obj = City()
        obj.name = "ALXAfrica"
        self.assertIn("name", obj.to_dict())

    def test_dict_with_arg(self):
        # test to check args in to_dict
        obj = City()
        with self.assertRaises(TypeError):
            obj.to_dict(None)

    def test_state_id_public(self):
        state1 = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(state1))
        self.assertNotIn("state_id", state1.__dict__)

    def test_str_method(self):
        # Testing the __str__ method
        obj_dt = datetime.now()
        obj_dt_r = repr(obj_dt)

        obj = City()
        obj.id = "8602393"
        obj.created_at = obj.updated_at = obj_dt

        obj_str = obj.__str__()

        self.assertIn("[City] (8602393)", obj_str)
        self.assertIn("'id': '8602393'", obj_str)
        self.assertIn("'created_at': " + obj_dt_r, obj_str)
        self.assertIn("'updated_at': " + obj_dt_r, obj_str)


class TestCity_save_method(unittest.TestCase):
    """ unittesting to check the save method """
=======
unittests for city class
of models
"""

import models
import unittest
from datetime import datetime
from time import sleep
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):
    """ Unittests for testing the city class """
    def test_id_public(self):
        self.assertEqual(str, type(City().id))

    def test_state_id_public(self):
        city = City()
        self.assertEqual(str, type(City.state_id))
        self.assertIn("state_id", dir(city))
        self.assertNotIn("state_id", city.__dict__)

    def test_update_at_public_datetime(self):
        self.assertEqual(datetime, type(City().updated_at))

    def test_name_public(self):
        city = City()
        self.assertEqual(str, type(City.name))
        self.assertIn("name", dir(city))
        self.assertNotIn("name", city.__dict__)

    def test_two_city_ids(self):
        city1 = City()
        city2 = City()
        self.assertNotEqual(city1.id, city2.id)

    def test_two_city_update_ats(self):
        city1 = City()
        sleep(0.05)
        city2 = City()
        self.assertLess(city1.updated_at, city2.updated_at)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        city = City()
        city.id = "8602393"
        city.created_at = city.updated_at = d_time
        city_str = city.__str__()
        self.assertIn("[City] (8602393)", city_str)
        self.assertIn("'created_at': " + d_time_r, city_str)
        self.assertIn("'updated_at': " + d_time_r, city_str)

    def test_to_dict(self):
        self.assertTrue(dict, type(City().to_dict()))

    def test_dict_with_added_attr(self):
        city = City()
        city.mid_name = "Blessing"
        city.num = 86
        self.assertEqual("Blessing", city.mid_name)
        self.assertIn("num", city.to_dict())

    def test_to_dict_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.to_dict(None)


class TestCity_saving(unittest.TestCase):
    """ Unittests to save method of the city class """
>>>>>>> upstream/ysg

    @classmethod
    def setUp(self):
        try:
<<<<<<< HEAD
            os.rename("file.ison", "tmp")
=======
            os.rename("file.json", "tmp")
>>>>>>> upstream/ysg
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

<<<<<<< HEAD
    def test_save_method(self):
        # Testing the saving method
        obj = BaseModel()
        old_updated_at = obj.updated_at
        obj.save()
        new_updated_at = obj.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_save_args(self):
        # test save args
        obj = City()
        with self.assertRaises(TypeError):
            obj.save(None)


if __name__ == '__main__':
=======
    def test_two_saves(self):
        city = City()
        sleep(0.05)
        f_updated_at = city.updated_at
        city.save()
        s_updated_at = city.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)
        city.save()
        self.assertLess(s_updated_at, city.updated_at)

    def test_save_with_args(self):
        city = City()
        with self.assertRaises(TypeError):
            city.save(None)

    def test_one_save(self):
        city = City()
        sleep(0.05)
        f_updated_at = city.updated_at
        city.save()
        self.assertLess(f_updated_at, city.updated_at)


if __name__ == "__main__":
>>>>>>> upstream/ysg
    unittest.main()
