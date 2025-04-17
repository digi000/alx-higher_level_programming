#!/usr/bin/python3
import unittest
mi = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(mi([1,2,3]), 3)
        self.assertEqual(mi([1,3,2]), 3)
        self.assertEqual(mi([]), None)

if __name__ == "__main__":
    unittest.main()
