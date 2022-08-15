# -*- encoding: utf-8 -*-
import unittest

from converter.converter import *


class temperature_conversion(unittest.TestCase):
    
    def test_cel_to_fahren(self):
        """
        # Testing function cel_to_fahren
        """
        self.assertEqual(cel_to_fahren(20), 68.0)
        self.assertEqual(cel_to_fahren(20.0), 68.0)
        self.assertEqual(cel_to_fahren(0), 32.0)
        self.assertEqual(cel_to_fahren(-10), 14.0)
        self.assertEqual(cel_to_fahren(-10.0), 14.0)
        self.assertEqual(cel_to_fahren(-40.0), -40.0)
    
    def test_fahren_to_cel(self):
        """
        # Testing function fahren_to_cel
        """
        self.assertEqual(fahren_to_cel(32), 0.0)
        self.assertEqual(fahren_to_cel(32.0), 0.0)
        self.assertEqual(fahren_to_cel(0), -17.8, msg='ERROR')
        self.assertEqual(fahren_to_cel(-13), -25.0)
        self.assertEqual(fahren_to_cel(-13.0), -25.0)
        self.assertEqual(fahren_to_cel(-40), -40.0)


if __name__ == '__main__':
    unittest.main()
