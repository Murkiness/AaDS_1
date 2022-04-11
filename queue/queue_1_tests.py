import unittest
from queue_1 import Queue


class TestQueue1(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()

        self.assertEqual(q.size(), 0)

        q.enqueue(1)
        q.enqueue(5)

        self.assertEqual(q.size(), 2)

    def test_dequeue(self):
        q = Queue()
        q.enqueue(1)
        q.enqueue(5)

        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 5)
        self.assertEqual(q.dequeue(), None)
