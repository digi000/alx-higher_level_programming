#!/usr/bin/python3
import unittest
mi = __import__("6-max_integer").max_integer
class TestMaxInteger(unittest.TestCase):
    def test_max_integer(self):
        self.assertEqual(mi([1,2,3]), 3)
        self.assertEqual(mi([1,3,2]), 3)
        self.assertEqual(mi([]), None)
        self.assertEqual(mi([-10, -20, -3, -40]), -3)
        self.assertEqual(mi([22]), 22)
        self.assertEqual(mi([5, 5, 5, 5]), 5)
        self.assertEqual(mi([10, 2, 3, 1]), 10)
        self.assertEqual(mi([1, 2, 3, 10]), 10)
        self.assertRaises(TypeError,mi,[1, "a", 3])

if __name__ == "__main__":
    unittest.main()
