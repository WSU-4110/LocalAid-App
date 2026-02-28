# test_user_helper.py

import unittest
from userhelper_class import UserHelper

class TestUserHelper(unittest.TestCase):
    def test_valid_username(self):
        helper = UserHelper("michelle")
        self.assertTrue(helper.is_valid_username())

    def test_invalid_username(self):
        helper = UserHelper("abc")
        self.assertFalse(helper.is_valid_username())

    def test_greet_user(self):
        helper = UserHelper("michelle")
        self.assertEqual(helper.greet_user(), "Welcome, michelle!")

    def test_uppercase(self):
        helper = UserHelper("michelle")
        self.assertEqual(helper.get_username_uppercase(), "MICHELLE")

    def test_has_numbers_true(self):
        helper = UserHelper("michelle123")
        self.assertTrue(helper.has_numbers())

    def test_has_numbers_false(self):
        helper = UserHelper("michelle")
        self.assertFalse(helper.has_numbers())

    def test_reverse_username(self):
        helper = UserHelper("michelle")
        self.assertEqual(helper.reverse_username(), "ellehcim")

if __name__ == '__main__':
    unittest.main()
