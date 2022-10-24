import unittest
import Journal


class MyTestCase(unittest.TestCase):
    def test_make_password(self):
        result = Journal.make_password()
        # self.assertEqual()
        print(result)

if __name__ == '__main__':
    unittest.main()
