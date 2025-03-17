import unittest
from functions import *

class test_password(unittest.TestCase):
    
    def test_length_of_lst(self):
        filename = "testFile.txt"
        lst = fromFileToLst(filename)

        self.assertEqual(len(lst), 18)


    def test_average(self):
        filename = "testFile.txt"
        average = 51.66666666667
        lst = fromFileToLst(filename)

        self.assertAlmostEqual(findAverage(lst), average)

    def test_false_average(self):
        filename = "testFile.txt"
        average = 30
        lst = fromFileToLst(filename)

        self.assertNotEqual(findAverage(lst), average)


if __name__ == '__main__':
    unittest.main()