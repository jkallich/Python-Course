import sys
sys.path.insert(0, "Happy_Numbers_Project")

import unittest
import Happy_Numbers

class HappyNumbersTestCase(unittest.TestCase):
    def test_square_and_add_nums(self):
        result = Happy_Numbers.square_and_add_nums(16)
        self.assertEqual(result, 37)

    def test_square_and_add_nums2(self):
        result = Happy_Numbers.square_and_add_nums(1)
        self.assertEqual(result, 1)

    def test_square_and_add_nums3(self):
        result = Happy_Numbers.square_and_add_nums(2)
        self.assertEqual(result, 4)

    def test_check_happy(self):
        result = Happy_Numbers.check_happy(11)
        self.assertEqual(result, False)

    def test_check_happy2(self):
        result = Happy_Numbers.check_happy(13)
        self.assertEqual(result, True)

    def test_make_nums_only(self):
        result = Happy_Numbers.make_nums_only(['56','76'])
        self.assertEqual(result, [56, 76])

    def test_make_nums_only(self):
        result = Happy_Numbers.make_nums_only(['56','76',' ',', ', ','])
        self.assertEqual(result, [56, 76])



if __name__ == '__main__':
    unittest.main()

