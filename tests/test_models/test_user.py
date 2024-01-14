#!/usr/bin/python3
"""
Unittest to test the user class
"""

import unittest
from time import sleep
import models
from models.user import User
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    """testing the User class"""

    def test_no_args(self):
        # test that there are no args
        self.assertEqual(User, type(User()))

    def test_instance_stored_in_obj(self):
        # test stored users
        self.assertIn(User(), models.storage.all().values())

    def test_id_public(self):
        # test if the id is a public string
        self.assertEqual(str, type(User().id))

    def test_email(self):
        # test if email is public
<<<<<<< HEAD
        self.assertEqual(str, type(User.email))
=======
        self.assertEqual(str, type(User.password))
>>>>>>> upstream/ysg

    def test_first_name(self):
        # test if first_name is public
        self.assertEqual(str, type(User.first_name))

    def test_last_name(self):
        # test if last_name is public
        self.assertEqual(str, type(User.last_name))

    def test_password(self):
        # test if password is public
        self.assertEqual(str, type(User.password))

    def test_attributes(self):
        # testing attributes
        user = User()
        self.assertTrue(hasattr(user, 'id'))
        self.assertTrue(hasattr(user, 'created_at'))
        self.assertTrue(hasattr(user, 'updated_at'))
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_str_representation(self):
        # test the str representation
        user = User()
        n_date = datetime.now()
        n_date_r = repr(n_date)
        user.id = "8602393"
        user.created_at = user.updated_at = n_date
        user_str = user.__str__()
        self.assertIn("[User] (8602393)", user_str)
        self.assertIn("'id': '8602393'", user_str)
        self.assertIn("'created_at': " + n_date_r, user_str)
        self.assertIn("'updated_at': " + n_date_r, user_str)

    def test_unique_ids(self):
        # test if any two ids are unique
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_user_created_at(self):
        # test if two users created at differen times
        user1 = User()
        sleep(0.1)
        user2 = User()
        self.assertLess(user1.created_at, user2.created_at)


class TestUser_save_method(unittest.TestCase):
    """ unittest for testing the saving of User class"""

    @classmethod
    def setUp(self):
        # setting up
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        # tearing down setUp
        try:
            os.remove("file.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass

    def test_one_save(self):
        user = User()
        sleep(0.05)
        f_updated_at = user.updated_at
        user.save()
        self.assertLess(f_updated_at, user.updated_at)

    def test_save_args(self):
        # test to save with args
        user = User()
        with self.assertRaises(TypeError):
            user.save(None)


if __name__ == '__main__':
    unittest.main()
