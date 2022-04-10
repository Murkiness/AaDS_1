import unittest
from stack_5 import check_brackets


class TestStack5(unittest.TestCase):

    def test_check_brackets_1(self):
        val = "()()()"
        self.assertTrue(check_brackets(val))

        val = "((()))"
        self.assertTrue(check_brackets(val))

    def test_check_brackets_2(self):
        val = "((()"
        self.assertFalse(check_brackets(val))

        val = "))(("
        self.assertFalse(check_brackets(val))
