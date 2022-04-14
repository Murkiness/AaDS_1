import unittest
from deque_1 import Deque


class TestDeque1(unittest.TestCase):

    def test_push_front_pop_tail(self):
        d = Deque()
        d.addFront(1)
        d.addFront(2)
        d.addFront(3)
        self.assertEqual(d.size(), 3)
        self.assertEqual(d.removeTail(), 1)
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.removeTail(), 2)
        self.assertEqual(d.removeTail(), 3)
        self.assertEqual(d.size(), 0)
        self.assertTrue(d.removeTail() is None)

    def test_push_tail_pop_front(self):
        d = Deque()
        d.addTail(1)
        d.addTail(2)
        d.addTail(3)
        self.assertEqual(d.removeFront(), 1)
        self.assertEqual(d.size(), 2)
        self.assertEqual(d.removeFront(), 2)
        self.assertEqual(d.removeFront(), 3)
        self.assertEqual(d.size(), 0)
        self.assertTrue(d.removeFront() is None)
