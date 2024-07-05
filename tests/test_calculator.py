import unittest
import os
import sys

sys.path.append('./packages')
from calculator import MD5Calculator

class TestMD5Calculator(unittest.TestCase):
    def setUp(self):
        # Set up a temporary file for testing
        self.test_file_name = 'temp_test_file.txt'
        with open(self.test_file_name, 'wb') as f:
            f.write(b'Hello World')

        # Expected MD5 hash for 'Hello World'
        self.expected_hash = 'b10a8db164e0754105b7a99be72e3fe5'

    def tearDown(self):
        # Clean up the temporary file after testing
        os.remove(self.test_file_name)

    def test_calculate(self):
        # Test the calculate method
        calculated_hash = MD5Calculator.calculate(self.test_file_name)
        self.assertEqual(calculated_hash, self.expected_hash)

if __name__ == '__main__':
    unittest.main()