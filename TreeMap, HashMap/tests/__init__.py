"""init file"""
import unittest

class MyTestCase(unittest.TestCase):
    """"something"""

    def test_something(self):
        """tests something"""
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
