import unittest
from deque_2 import is_palindrome


class TestDeque2(unittest.TestCase):

    def test_palindrome(self):
        words = ["abba", "adrda", "a", "aa"]

        for w in words:
            self.assertTrue(is_palindrome(w))

    def test_not_palindrome(self):
        words = ["orda", "adrsa", "art"]

        for w in words:
            self.assertFalse(is_palindrome(w))
