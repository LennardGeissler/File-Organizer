import os
import shutil
import unittest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from folder_mover import move_existing_folders_to_category
from categories import folder_categories

class TestFolderMover(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir, exist_ok=True)

        self.sample_folders = {
            'pdf': ['file1.pdf', 'file2.pdf'],
            'png': ['file1.png'],
        }

        for folder, files in self.sample_folders.items():
            folder_path = os.path.join(self.test_dir, folder)
            os.makedirs(folder_path, exist_ok=True)

            for file in files:
                with open(os.path.join(folder_path, file), 'w') as f:
                    f.write(f"Test content for {file}")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_move_existing_folders_to_category(self):
        move_existing_folders_to_category(self.test_dir)

        for folder in self.sample_folders.keys():
            expected_category = 'Documents' if folder == 'pdf' else 'Images'
            category_folder = os.path.join(self.test_dir, expected_category, folder)
            self.assertTrue(os.path.exists(category_folder))

if __name__ == "__main__":
    unittest.main()
