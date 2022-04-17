import unittest
from ordered_list import OrderedList


class TestOrderedList(unittest.TestCase):

    def test_add_asc(self):
        ol = OrderedList(True)
        ol.add(5)

        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.tail.value, 5)

        ol.add(4)
        self.assertEqual(ol.head.value, 4)
        self.assertEqual(ol.tail.value, 5)

        ol.add(88)
        self.assertEqual(ol.head.value, 4)
        self.assertEqual(ol.tail.value, 88)

        ol.add(77)
        self.assertEqual(ol.head.value, 4)
        self.assertEqual(ol.tail.value, 88)

        self.assertTrue(ol.head.prev is None)
        self.assertTrue(ol.tail.next is None)

        self.assertEqual(len(ol.get_all()), 4)

    def test_add_desc(self):
        ol = OrderedList(False)
        ol.add(5)
        ol.add(4)

        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.tail.value, 4)

        ol.add(88)
        self.assertEqual(ol.head.value, 88)
        self.assertEqual(ol.tail.value, 4)

        ol.add(77)
        self.assertEqual(ol.head.value, 88)
        self.assertEqual(ol.tail.value, 4)

        all = list(map(lambda x: x.value, ol.get_all()))

        self.assertEqual(all, [88, 77, 5, 4])

    def test_delete_asc(self):
        ol = OrderedList(True)
        ol.add(5)
        ol.add(3)
        ol.add(7)

        self.assertEqual(ol.find(5).value, 5)
        ol.delete(5)
        self.assertTrue(ol.find(5) is None)
        self.assertEqual(ol.find(3).value, 3)
        self.assertEqual(ol.find(7).value, 7)

    def test_delete_desc(self):
        ol = OrderedList(False)
        ol.add(5)
        ol.add(3)
        ol.add(7)

        self.assertEqual(ol.find(5).value, 5)
        ol.delete(5)
        self.assertTrue(ol.find(5) is None)
        self.assertEqual(ol.find(3).value, 3)
        self.assertEqual(ol.find(7).value, 7)

    def test_find_asc(self):
        ol = OrderedList(True)
        ol.add(5)
        ol.add(3)
        ol.add(7)

        self.assertEqual(ol.find(5).value, 5)
        self.assertEqual(ol.find(7).value, 7)
        self.assertTrue(ol.find(99) is None)

    def test_find_desc(self):
        ol = OrderedList(False)
        ol.add(5)
        ol.add(3)
        ol.add(7)

        self.assertEqual(ol.find(5).value, 5)
        self.assertEqual(ol.find(7).value, 7)
        self.assertTrue(ol.find(99) is None)

    def test_find_after_delete(self):
        ol = OrderedList(True)
        ol.add(5)
        ol.add(3)
        ol.add(7)

        all = list(map(lambda x: x.value, ol.get_all()))

        self.assertEqual(all, [3, 5, 7])

        for i in [3, 5, 7]:
            ol.delete(i)

        for i in [3, 5, 7]:
            self.assertTrue(ol.find(i) is None)

        self.assertTrue(ol.head is None)
        self.assertTrue(ol.tail is None)
