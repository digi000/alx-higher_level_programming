from models.rectangle import Rectangle as rt
import unittest

class TestRectangle(unittest.TestCase):
    def test_area(self):
        r1 = rt(3,5)
        self.assertEqual(r1.area(), 15)
