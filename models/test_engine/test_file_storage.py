#!/usr/bin/python3

"""
unittesting how FileStorage class work
with all other classes
"""

import models
from datetime import datetime
import os
from os import path
import unittest
from models.base_model import BaseModel
from models.user import User
from models.place import Place
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """ class to test File storage class"""
    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmpo")
        except IOError:
            pass
        self.storage = FileStorage()
        FileStorage._FileStorage__objects = {}

    @classmethod
    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmpo", "file.json")
        except IOError:
            pass

    def test_all(self):
        # test all storage
        storage = FileStorage()
        obj_dict = storage.all()
        self.assertIsNotNone(obj_dict)
        self.assertEqual(type(obj_dict), dict)
        self.assertIs(obj_dict, storage._FileStorage__objects)

    def test_new_no_args(self):
        with self.assertRaises(TypeError):
            self.storage.new()

    def test_variables(self):
        # testing variables of class
        f1 = FileStorage()
        list_them = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for ex in f1.all().values():
            list_them.append(ex)
        for ex in list_them:
            del f1.all()[ex.__class__.__name__ + '.' + ex.id]

        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertFalse(hasattr(f1, '__file_path'))
        self.assertFalse(hasattr(f1, '__objects'))
        del f1
        if os.path.exists('file.json'):
            print('file still exists')
            os.remove('file.json')

    def test_new(self):
        # test for new User
        user = User()
        self.storage.new(user)
        # obj_dict = self.storage.all()
        # self.assertEqual(len(obj_dict), 1)
        self.assertIn("User." + user.id, self.storage.all())

    def test_new_objects(self):
        # testing objects
        self.storage._FileStorage__objects = {}
        self.assertEqual(self.storage._FileStorage__objects, {})
        obj = BaseModel()
        self.storage.new(obj)
        obj1 = self.storage.all()
        self.assertIn("BaseModel.{}".format(obj.id), obj1)
        self.assertEqual(obj1["BaseModel.{}".format(obj.id)], obj)

    def test_type_obj(self):
        # test obj type
        self.assertIs(type(FileStorage._FileStorage__objects), dict)

    def test_path_of_file(self):
        # test file path
        self.assertEqual(self.storage._FileStorage__file_path, "file.json")

    def test_new_class(self):
        f1 = BaseModel(id="861")
        f1_key = 'BaseModel.' + f1.id
        f2 = User(id="01")
        f2_key = 'User.' + f2.id
        f3 = City(id="02")
        f3_key = 'City.' + f3.id
        f4 = Amenity(id="03")
        f4_key = 'Amenity.' + f4.id
        f5 = Place(id='04')
        f5_key = 'Place.' + f5.id
        f6 = Review(id='05')
        f6_key = 'Review.' + f6.id
        f7 = State(id='06')
        f7_key = 'State.' + f7.id

        self.assertEqual(self.storage.all(), {})
        f1.id = 861
        self.storage.new(f1)
        self.storage.new(f2)
        self.storage.new(f3)
        self.storage.new(f4)
        self.storage.new(f5)
        self.storage.new(f6)
        self.storage.new(f7)
        self.assertEqual(f1, self.storage.all()[f1_key])
        self.assertEqual(f2, self.storage.all()[f2_key])
        self.assertEqual(f3, self.storage.all()[f3_key])
        self.assertEqual(f4, self.storage.all()[f4_key])
        self.assertEqual(f5, self.storage.all()[f5_key])
        self.assertEqual(f6, self.storage.all()[f6_key])
        self.assertEqual(f7, self.storage.all()[f7_key])

    def test_save_file_existence(self):
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        f1 = BaseModel()
        f1_key = 'BaseModel.' + f1.id
        f2 = User()
        f2_key = 'User.' + f2.id
        f3 = City()
        f3_key = 'City.' + f3.id
        f4 = Amenity()
        f4_key = 'Amenity.' + f4.id
        f5 = Place()
        f5_key = 'Place.' + f5.id
        f6 = Review()
        f6_key = 'Review.' + f6.id
        f7 = State()
        f7_key = 'State.' + f7.id
        self.storage.save()
        # self.assertTrue(path.isfile("file.json"))
        # FileStorage._FileStorage__objects = {}

        self.storage.reload()

        self.assertTrue(f1_key in self.storage.all().keys())
        self.assertEqual(f1.id, self.storage.all()[f1_key].id)
        self.assertTrue(f2_key in self.storage.all().keys())
        self.assertEqual(f2.id, self.storage.all()[f2_key].id)
        self.assertTrue(f3_key in self.storage.all().keys())
        self.assertEqual(f3.id, self.storage.all()[f3_key].id)
        self.assertTrue(f4_key in self.storage.all().keys())
        self.assertEqual(f4.id, self.storage.all()[f4_key].id)
        self.assertTrue(f5_key in self.storage.all().keys())
        self.assertEqual(f5.id, self.storage.all()[f5_key].id)
        self.assertTrue(f6_key in self.storage.all().keys())
        self.assertEqual(f6.id, self.storage.all()[f6_key].id)
        self.assertTrue(f7_key in self.storage.all().keys())
        self.assertEqual(f7.id, self.storage.all()[f7_key].id)

    def test_storage_save(self):
        # saving
        obj1 = BaseModel()
        self.storage.save()
        with open("file.json", "r") as f:
            self.assertIn("BaseModel.{}".format(obj1.id), f.read())


if __name__ == '__main__':
    unittest.main()
