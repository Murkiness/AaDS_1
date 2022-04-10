import unittest
from stack_2 import Stack


class TestStack2(unittest.TestCase):

    def test_size(self):
        s = Stack()
        self.assertEqual(s.size(), 0)
        s.push(1)
        s.push(2)
        self.assertEqual(s.size(), 2)

    def test_pop_empty(self):
        s = Stack()
        self.assertTrue(s.pop() is None)

    def test_pop_non_empty(self):
        s = Stack()
        s.push(1)
        s.push(2)

        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek(self):
        s = Stack()
        self.assertTrue(s.peek() is None)
        s.push(1)
        s.push(2)

        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.peek(), 2)
