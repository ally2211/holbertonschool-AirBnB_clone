#!/usr/bin/python3

import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    def test_to_dict(self):
        # test if to_dict returns correct dictionary representation
        pass

    def test_save(self):
        # test if save updates `updated_at` and saves to file
        pass

    def test_str(self):
        # test if __str__ returns expected string representation
        pass

if __name__ == "__main__":
    unittest.main()

