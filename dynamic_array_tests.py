import unittest
from dynamic_array import DynArray


class TestDynamicArray(unittest.TestCase):

    def make_array(self, upper_range_limit):
        da = DynArray()
        for i in range(upper_range_limit):
            da.append(i)

        return da

    def test_insert_no_buffer_change(self):
        da = self.make_array(5)
        da.insert(5, 5)
        self.assertEqual(da.count, 6)
        self.assertEqual(da.capacity, 16)
        for i in range(6):
            self.assertEqual(da[i], i)

        da = self.make_array(15)
        da.insert(5, 25)
        self.assertEqual(da.count, 16)
        self.assertEqual(da.capacity, 16)
        for i in range(5):
            self.assertEqual(da[i], i)
        self.assertEqual(da[5], 25)
        for i in range(6, 15):
            self.assertEqual(da[i], i-1)

    def test_insert_no_buffer_change_after_edge(self):
        da = self.make_array(15)
        da.insert(15, 50)
        self.assertEqual(da.count, 16)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da[da.count-1], 50)

    def test_insert_buffer_change(self):
        da = self.make_array(16)
        da.insert(5, 50)
        self.assertEqual(da.count, 17)
        self.assertEqual(da.capacity, 32)
        for i in range(5):
            self.assertEqual(da[i], i)
        self.assertEqual(da[5], 50)
        for i in range(6, 17):
            self.assertEqual(da[i], i-1)

    def test_insert_index_error(self):
        da = self.make_array(5)

        with self.assertRaises(IndexError):
            da.insert(-1, 20)

        with self.assertRaises(IndexError):
            da.insert(6, 21)

    def test_delete_index_error(self):
        da = self.make_array(5)
        with self.assertRaises(IndexError):
            da.delete(-1)

        with self.assertRaises(IndexError):
            da.delete(6)

    def test_delete_no_buffer_change(self):
        da = self.make_array(100)
        for i in range(20):
            da.delete(0)

        self.assertEqual(da.count, 80)
        self.assertEqual(da.capacity, 128)

    def test_delete_no_buffer_change_when_lowest_capacity(self):
        da = self.make_array(10)
        for i in range(9, 1, -1):
            da.delete(i)

        self.assertEqual(da.count, 2)
        self.assertEqual(da.capacity, 16)

    def test_delete_buffer_change(self):
        da = self.make_array(100)
        for i in range(36):
            da.delete(0)

        self.assertEqual(da.count, 64)
        self.assertEqual(da.capacity, 128)

        da.delete(0)
        self.assertEqual(da.count, 63)
        self.assertEqual(da.capacity, 85)
