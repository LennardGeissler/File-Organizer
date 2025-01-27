import os
import shutil
import unittest
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from file_organizer import organize_files
from categories import file_categories

class TestFileOrganizer(unittest.TestCase):

    def setUp(self):
        self.test_dir = "test_directory"
        os.makedirs(self.test_dir, exist_ok=True)

        self.sample_files = {
            'Images': ['image1.jpg', 'image2.png'],
            'Documents': ['doc1.pdf', 'doc2.txt'],
            'Videos': ['video1.mp4'],
            'Archives': ['archive1.zip'],
            'Other': ['randomfile.xyz']
        }

        for category, files in self.sample_files.items():
            for file in files:
                with open(os.path.join(self.test_dir, file), 'w') as f:
                    f.write(f"Test content for {file}")

    def tearDown(self):
        shutil.rmtree(self.test_dir)

    def test_organize_files(self):
        organize_files(self.test_dir, file_types=[])
        for category, files in self.sample_files.items():
            category_dir = os.path.join(self.test_dir, category)
            self.assertTrue(os.path.exists(category_dir))

            for file in files:
                file_path = os.path.join(category_dir, file)
                if category != 'Other':
                    self.assertTrue(os.path.exists(file_path))
                else:
                    self.assertTrue(os.path.exists(os.path.join(self.test_dir, 'Other', file)))

if __name__ == "__main__":
    unittest.main()
