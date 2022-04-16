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

    def test_add_desc(self):
        ol = OrderedList(False)
        ol.add(5)
        ol.add(4)

        self.assertEqual(ol.head.value, 5)
        self.assertEqual(ol.tail.value, 4)

        ol.add(88)
        self.assertEqual(ol.head.value, 88)
        self.assertEqual(ol.tail.value, 4)

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
