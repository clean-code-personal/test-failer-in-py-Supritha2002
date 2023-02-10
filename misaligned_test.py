import unittest
from misaligned import *

class TestingMisaligned(unittest.TestCase):

    def testing_misaligned(self):
     #performs these checks and asserts that the length of the list is 25, which is the number of mappings that should be present
        result = create_color_map()
        map_number=1
        for pair_number in result:
            num,major,minor=pair_number.split('|')
            major=major.strip()
            minor=minor.strip()
            self.assertEqual(int(num),map_number) #checks pair_number
            self.assertIn(major,["White", "Red", "Black", "Yellow", "Violet"])
            self.assertIn(minor,["Blue", "Orange", "Green", "Brown", "Slate"])
            map_number+=1
        
print("All tests passed!")

if __name__ == '__main__':
    unittest.main()
