# -*- encoding: utf-8 -*-
import unittest

from converter.converter import celsius_to_fahrenheit, fahrenheit_to_celsius
from converter.utils import is_float


class test_temperature_conversion(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        """
        Testing function celsius_to_fahrenheit
        """
        self.assertEqual(celsius_to_fahrenheit(20), 68.0)
        self.assertEqual(celsius_to_fahrenheit(20.0), 68.0)
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)
        self.assertEqual(celsius_to_fahrenheit(-10), 14.0)
        self.assertEqual(celsius_to_fahrenheit(-10.0), 14.0)
        self.assertEqual(celsius_to_fahrenheit(-40.0), -40.0)

    def test_fahrenheit_to_celsius(self):
        """
        Testing function fahrenheit_to_celsius
        """
        self.assertEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertEqual(fahrenheit_to_celsius(32.0), 0.0)
        self.assertEqual(fahrenheit_to_celsius(0), -17.8, msg='ERROR')
        self.assertEqual(fahrenheit_to_celsius(-13), -25.0)
        self.assertEqual(fahrenheit_to_celsius(-13.0), -25.0)
        self.assertEqual(fahrenheit_to_celsius(-40), -40.0)

    def test_is_float(self):
        """
        Testing function is_float
        """
        self.assertTrue(is_float(0), msg="Failed")
        self.assertTrue(is_float(0.0))
        self.assertTrue(is_float(-0.0))
        self.assertTrue(is_float(10))
        self.assertTrue(is_float(-10.55))

        self.assertFalse(is_float("asa"))
        self.assertFalse(is_float("ass1000asa"))
        self.assertTrue(is_float("10.0"))
        self.assertTrue(is_float("-0.0"))
        self.assertTrue(is_float("   -0.0  "))
        self.assertTrue(is_float("\u0038"))  # Unicode char for 8
        self.assertFalse(is_float("\u0038\u0061"))  # Unicode char 8a


if __name__ == '__main__':
    unittest.main()
