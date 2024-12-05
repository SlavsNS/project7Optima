import unittest
import os
from Infra.data import DataManager

class TestDataManager(unittest.TestCase):
    def setUp(self):
        self.filename = "test_data.json"
        self.test_data = {"key": "value"}

    def tearDown(self):
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_save_to_file(self):
        DataManager.save_to_file(self.test_data, self.filename)
        self.assertTrue(os.path.exists(self.filename))

    def test_load_from_file(self):
        DataManager.save_to_file(self.test_data, self.filename)
        loaded_data = DataManager.load_from_file(self.filename)
        self.assertEqual(loaded_data, self.test_data)

if __name__ == "__main__":
    unittest.main()
