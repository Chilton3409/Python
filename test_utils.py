#!/usr/bin/env python3
#New file created
import unittest

import utils


class TestUtils(unittest.TestCase):
    def test_is_prime(self):
        self.assertFalse(utils.is_prime(4))
        self.assertTrue(utils.is_prime(2))
        self.assertTrue(utils.is_prime(3))
        self.assertFalse(utils.is_prime(8))
        self.assertFalse(utils.is_prime(10))
        self.assertTrue(utils.is_prime(7))
        self.assertEqual(utils.is_prime(-3),
                         "Negative numbers are not allowed")

    def test_cubic(self):
        self.assertEqual(utils.cubic(2), 8)
        self.assertEqual(utils.cubic(-2), -8)
        self.assertNotEqual(utils.cubic(2), 4)
        self.assertNotEqual(utils.cubic(-3), 27)

    def test_say_hello(self):
        self.assertEqual(utils.say_hello("Geekflare"), "Hello, Geekflare")
        self.assertEqual(utils.say_hello("Chandan"), "Hello, Chandan")
        self.assertNotEqual(utils.say_hello("Chandan"), "Hi, Chandan")
        self.assertNotEqual(utils.say_hello("Hafeez"), "Hi, Hafeez")



if __name__ == '__main__':
    unittest.main()