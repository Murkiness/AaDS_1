import unittest
from linked_list import *


class TestLinkedList(unittest.TestCase):

    def build_list(self, array):
        list = LinkedList()
        for el in array:
            list.add_in_tail(Node(el))

        return list

    def setUp(self):
        self.linked_list = self.build_list([5, 6, 5, 50, 5])

    def test_get_list_as_array_with_elements(self):
        ll = self.build_list([1])
        res = ll.get_list_as_array()
        self.assertEqual(res, [1])
        self.assertEqual(self.linked_list.get_list_as_array(), [5, 6, 5, 50, 5])

    def test_get_list_as_array_wo_elements(self):
        ll = LinkedList()
        res = ll.get_list_as_array()
        self.assertEqual(res, None)

    def test_delete_one_element(self):
        self.linked_list.delete(5)
        self.assertEqual(self.linked_list.get_list_as_array(), [6, 5, 50, 5])
        self.assertEqual(self.linked_list.head.value, 6)
        self.assertTrue(self.linked_list.tail is not None)

    def test_delete_all_similar_elements(self):
        self.linked_list.delete(5, True)
        self.assertEqual(self.linked_list.get_list_as_array(), [6, 50])
        self.assertEqual(self.linked_list.head.value, 6)
        self.assertEqual(self.linked_list.tail.value, 50)
        self.assertTrue(self.linked_list.tail is not None)
        self.assertTrue(self.linked_list.tail.value == 50)

    def test_delete_does_nothing_on_empty_list(self):
        ll = LinkedList()
        ll.delete(6)
        res = ll.get_list_as_array()
        self.assertEqual(res, None)

    def test_delete_does_nothing_for_non_existent_element(self):
        self.linked_list.delete(111, True)
        self.assertTrue(self.linked_list.tail is not None)
        self.assertTrue(self.linked_list.tail.value == 5)
        self.assertTrue(self.linked_list.head is not None)
        self.assertTrue(self.linked_list.head.value == 5)

    def test_delete_all_for_mono_list(self):
        ll = self.build_list([4, 4, 4])
        ll.delete(4, True)
        self.assertTrue(ll.head is None)
        self.assertTrue(ll.tail is None)

    def test_delete_all_similar_elements_2(self):
        ll = self.build_list([4, 4, 5])
        ll.delete(4, True)
        self.assertTrue(ll.head is not None)
        self.assertTrue(ll.tail is not None)
        self.assertTrue(ll.tail is ll.head)

    def test_delete_all_similar_elements_3(self):
        ll = self.build_list([4, 5, 5])
        ll.delete(5, True)
        self.assertTrue(ll.head is not None)
        self.assertTrue(ll.tail is not None)
        self.assertTrue(ll.tail is ll.head)

    def test_clean(self):
        ll = LinkedList()

        for l_list in [ll, self.linked_list]:
            with self.subTest(li=l_list):
                l_list.clean()
                self.assertEqual(l_list.head, None)
                self.assertEqual(l_list.tail, None)

    def test_len_for_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.len(), 0)

    def test_len_for_one_element_list(self):
        ll = self.build_list([1])
        self.assertEqual(ll.len(), 1)

    def test_len_for_several_element_list(self):
        self.assertEqual(self.linked_list.len(), 5)

    def test_find_all_with_empty_list(self):
        ll = LinkedList()
        self.assertEqual(ll.find_all(0), [])

    def test_find_all_with_one_element(self):
        ll = self.build_list([1])
        self.assertEqual(ll.find_all(0), [])
        res = ll.find_all(1)
        self.assertEqual(len(res), 1)
        self.assertTrue(res[0].value == 1)

    def test_find_all_with_several_elements(self):
        res1 = self.linked_list.find_all(5)
        self.assertEqual(len(res1), 3)
        for n in res1:
            self.assertTrue(n.value == 5)

        res2 = self.linked_list.find_all(50)
        self.assertEqual(len(res2), 1)
        self.assertTrue(res2[0].value == 50)

    def test_insert_in_empty_list(self):
        ll = LinkedList()
        n = Node(7)
        ll.insert(None, n)
        self.assertTrue(ll.head == n)
        self.assertTrue(ll.tail == n)

    def test_insert_as_first_element(self):
        n = Node(7)
        self.linked_list.insert(None, n)
        self.assertEqual(self.linked_list.get_list_as_array(), [7, 5, 6, 5, 50, 5])
        self.assertTrue(self.linked_list.head is n)

    def test_insert_as_last_element(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        ll.insert(None, n1)
        ll.insert(n1, n2)
        self.assertEqual(ll.get_list_as_array(), [1, 2])
        self.assertTrue(ll.tail is n2)

    def test_insert_in_the_middle(self):
        ll = LinkedList()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        ll.insert(None, n1)
        ll.insert(n1, n2)
        ll.insert(n1, n3)
        self.assertEqual(ll.get_list_as_array(), [1, 3, 2])
        self.assertTrue(ll.tail is n2)
        self.assertTrue(ll.head is n1)

    def test_sum_lists_equal_length(self):
        list2 = self.build_list([9, 8, 3, 11, 15])
        res = sum_lists(list2, self.linked_list)
        self.assertEqual(res.get_list_as_array(), [14, 14, 8, 61, 20])
        self.assertTrue(res.head.value == 14)
        self.assertTrue(res.tail.value == 20)

    def test_sum_lists_one_el(self):
        ll1 = self.build_list([1])
        ll2 = self.build_list([2])
        res = sum_lists(ll1, ll2)
        self.assertTrue(res.head is res.tail)
        self.assertTrue(res.head is not None)
        self.assertTrue(res.head.next is None)

    def test_sum_lists_not_equal_length(self):
        list2 = self.build_list([9])
        res = sum_lists(list2, self.linked_list)
        self.assertTrue(res is None)
        res2 = sum_lists(self.linked_list, list2)
        self.assertTrue(res2 is None)

    def test_sum_lists_with_empty(self):
        ll1 = LinkedList()
        ll2 = LinkedList()
        res1 = sum_lists(ll1, ll2)
        res2 = sum_lists(ll1, self.linked_list)
        res3 = sum_lists(self.linked_list, ll1)

        for r in [res1, res2, res3]:
            self.assertTrue(r is None)


if __name__ == '__main__':
    unittest.main()
