import unittest
import tempfile
import os
import shutil
import sys

sys.path.append('./packages')
from folder_synchronization import FolderSynchronizer

class TestFolderSynchronizer(unittest.TestCase):
    def setUp(self):
        # Create temporary directories for source and replica
        self.source_dir = tempfile.mkdtemp()
        self.replica_dir = tempfile.mkdtemp()

        # Create a test file in the source directory
        self.test_file_name = "test_file.txt"
        test_file_path = os.path.join(self.source_dir, self.test_file_name)
        with open(test_file_path, "w") as f:
            f.write("Hello, World!")

    def tearDown(self):
        # Remove temporary directories
        shutil.rmtree(self.source_dir)
        shutil.rmtree(self.replica_dir)

    def test_sync(self):
        # Instantiate FolderSynchronizer and run sync
        synchronizer = FolderSynchronizer(self.source_dir, self.replica_dir, 1)
        synchronizer.sync()

        # Check if the file exists in the replica directory
        replica_file_path = os.path.join(self.replica_dir, self.test_file_name)
        self.assertTrue(os.path.exists(replica_file_path))

        # Verify the file contents are the same
        with open(replica_file_path, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello, World!")

if __name__ == '__main__':
    unittest.main()