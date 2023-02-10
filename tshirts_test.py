import unittest
from tshirts import *

class TestTshirts(unittest.TestCase):

    def test_tshirts(self):
        self.assertEqual(size(38), 'S')
        self.assertEqual(size(37), 'S')
        self.assertEqual(size(40), 'M')
        self.assertEqual(size(43), 'L')
print("All is well (maybe!)\n")
if __name__ == '__main__':
    unittest.main()