import os
import shutil
import unittest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from duplicate_finder import find_duplicates, show_and_remove_duplicates

class TestDuplicateFinder(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir, exist_ok=True)

        # Create files, including duplicates
        self.original_file = os.path.join(self.test_dir, 'file1.txt')
        self.duplicate_file = os.path.join(self.test_dir, 'file1_duplicate.txt')

        with open(self.original_file, 'w') as f:
            f.write("This is a test file.")

        shutil.copy(self.original_file, self.duplicate_file)

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_find_duplicates(self):
        duplicates = find_duplicates(self.test_dir)
        self.assertEqual(len(duplicates), 1)
        self.assertEqual(duplicates[0][1], self.duplicate_file)

    def test_show_and_remove_duplicates(self):
        show_and_remove_duplicates(self.test_dir)
        self.assertFalse(os.path.exists(self.duplicate_file))

if __name__ == "__main__":
    unittest.main()
