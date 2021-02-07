#!/usr/bin/env python

import unittest
import div_by_3

class TestDivBy3(unittest.TestCase):

    def test_divisble_by_3(self):
        self.assertEqual(div_by_3.divisible_by_3(15), "aunty")
        self.assertEqual(div_by_3.divisible_by_3(5), "uncle")
        self.assertEqual(div_by_3.divisible_by_3(15.5), "uncle")
        self.assertEqual(div_by_3.divisible_by_3(0), "aunty")
        
        with self.assertRaises(TypeError):
            div_by_3.divisible_by_3("somestring")

if __name__ == "__main__":
    unittest.main()