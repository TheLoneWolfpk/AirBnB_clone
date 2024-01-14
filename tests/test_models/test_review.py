#!/usr/bin/python3
"""
Unittesting the review class
"""

import models
import unittest
from datetime import datetime
import os
from time import sleep
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Unittesting for the Review class
    """
    def test_new_inst_stored(self):
        self.assertIn(Review(), models.storage.all().values())

    def test_place_id_public(self):
        rev = Review()
        self.assertEqual(str, type(Review.place_id))
        self.assertIn("place_id", dir(rev))
        self.assertNotIn("place_id", rev.__dict__)

    def test_unique_review(self):
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

    def test_str_repr(self):
        d_time = datetime.now()
        d_time_r = repr(d_time)
        rev = Review()
        rev.id = "8602393"
        rev.created_at = rev.updated_at = d_time
        rev_str = rev.__str__()
        self.assertIn("[Review] (8602393)", rev_str)
        self.assertIn("'created_at': " + d_time_r, rev_str)
        self.assertIn("'updated_at': " + d_time_r, rev_str)

<<<<<<< HEAD
=======
    def test_unique_review_id(self):
        """check if two reviews are unique"""
        rev1 = Review()
        rev2 = Review()
        self.assertNotEqual(rev1.id, rev2.id)

>>>>>>> upstream/ysg
    def test_inst_with_kwargs(self):
        d_time = datetime.now()
        d_time_i = d_time.isoformat()
        rev = Review(id="861", created_at=d_time_i, updated_at=d_time_i)
        self.assertEqual(rev.id, "861")
        self.assertEqual(rev.created_at, d_time)
        self.assertEqual(rev.updated_at, d_time)

<<<<<<< HEAD
=======
    def test_diff_in_created_at(self):
        """test differences in review creation time"""
        rev1 = Review()
        sleep(0.05)  # wait a bit
        rev2 = Review()
        self.assertLess(rev1.created_at, rev2.created_at)

    def test_diff_in_updated_at(self):
        """test differences in review update times"""
        rev1 = Review()
        sleep(0.05)  # wait a bit
        rev2 = Review()
        self.assertLess(rev1.updated_at, rev2.updated_at)

    def test_text_public(self):
        """test if text of review is public"""
        rev = Review()
        self.assertEqual(str, type(Review.text))
        self.assertIn("text", dir(rev))
        self.assertNotIn("text", rev.__dict__)

    def test_dict(self):
        """ to test the to_dict funciton """
        self.assertTrue(dict, type(Review().to_dict()))

    def test_dict_keys(self):
        """ test if to_dict had correct keys"""
        rev = Review()
        self.assertIn("id", rev.to_dict())
        self.assertIn("created_at", rev.to_dict())
        self.assertIn("updated_at", rev.to_dict())
        self.assertIn("__class__", rev.to_dict())

    def test_dict_added(self):
        """ test to_dict for added attributes"""
        rev = Review()
        rev.m_name = "Kobby"
        rev.num = 65
        self.assertEqual("Kobby", rev.m_name)
        self.assertIn("num", rev.to_dict())

    def test_dict_datetime_attributes(self):
        """test to_dict datetime are strings"""
        rev = Review()
        rev_dict = rev.to_dict()
        self.assertEqual(str, type(rev_dict["id"]))
        self.assertEqual(str, type(rev_dict["created_at"]))
        self.assertEqual(str, type(rev_dict["updated_at"]))

    def test_dict_args(self):
        """test to_dict with args"""
        rev = Review()
        with self.assertRaises(TypeError):
            rev.to_dict(None)

    def test_dict_output(self):
        d_time = datetime.now()
        rev = Review()
        rev.id = "8602393"
        rev.created_at = rev.updated_at = d_time
        d_dict = {
                'id': '8602393',
                '__class__': 'Review',
                'created_at': d_time.isoformat(),
                'updated_at': d_time.isoformat(),
        }
        self.assertDictEqual(rev.to_dict(), d_dict)

    def test_inst_None_kwargs(self):
        """test instantiation of no kwargs"""
        with self.assertRaises(TypeError):
            Review(id=None, created_at=None, updated_at=None)


class TestReview_saving(unittest.TestCase):
    """ save the review"""

    @classmethod
    def setUp(self):
        try:
            os.rename("file.json", "tmpo")
        except IOError:
            pass

    @classmethod
    def tearDown(self):
        # tear down the temporary setup
        try:
            os.remove("file.json")  # remove the json update
        except IOError:
            pass
        try:
            os.rename("tmpo", "file.json")
        except IOError:
            pass

    def test_save_a_review(self):
        rev = Review()
        sleep(0.05)  # wait a bit
        f_updated_at = rev.updated_at
        rev.save()
        self.assertLess(f_updated_at, rev.updated_at)

    def test_save_two_reviews(self):
        rev = Review()
        sleep(0.05)  # wait for the next save
        f_updated_at = rev.updated_at
        rev.save()
        s_updated_at = rev.updated_at
        self.assertLess(f_updated_at, s_updated_at)
        sleep(0.05)  # wait for the next save
        rev.save()

    def test_Update_file_saving(self):
        rev = Review()
        rev.save()  # test save
        rev_id = "Review." + rev.id
        with open("file.json", "r") as f:
            self.assertIn(rev_id, f.read())

>>>>>>> upstream/ysg

if '__name__' == '__main__':
    unittest.main()
