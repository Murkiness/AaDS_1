import unittest
from linked_list2_upgrade import LinkedList2, Node


class TestLinkedList2(unittest.TestCase):

    def check_list_consistency(self, list):
        r1 = list.value_list_from_head()
        r2 = list.value_list_from_tail()
        r2.reverse()
        self.assertEqual(r1, r2)

    def build_list(self, array):
        list = LinkedList2()
        for el in array:
            list.add_in_tail(Node(el))

        return list

    def test_len(self):
        l1 = LinkedList2()
        self.assertTrue(l1.len() == 0)

        l2 = self.build_list([2, 3])
        self.assertTrue(l2.len() == 2)

    def test_clean(self):
        l2 = self.build_list([2, 3])
        self.assertTrue(l2.len() == 2)
        l2.clean()
        self.assertTrue(l2.len() == 0)

    def test_find(self):
        l1 = LinkedList2()
        self.assertTrue(l1.find(10) is None)

        l2 = self.build_list([2, 3])
        self.assertTrue(l2.find(2).value == 2)

    def test_find_all(self):
        l1 = self.build_list([2, 3, 7, 2])
        self.assertTrue(len(l1.find_all(2)) == 2)
        self.assertTrue(len(l1.find_all(7)) == 1)
        self.assertTrue(len(l1.find_all(8)) == 0)

    def test_delete_1(self):
        l1 = self.build_list([1, 2, 3, 4, 2])
        l1.delete(3)
        self.check_list_consistency(l1)

    def test_delete_2(self):
        l1 = self.build_list([1, 2, 3, 4, 2])
        l1.delete(2, True)
        self.check_list_consistency(l1)
        self.assertEqual(l1.len(), 3)
        self.assertTrue(l1.find(2) is None)

    def test_insert_1(self):
        l1 = LinkedList2()
        l1.insert(None, Node(3))
        self.check_list_consistency(l1)
        self.assertTrue(l1.find(3) is not None)

    def test_insert_2(self):
        l1 = self.build_list([1, 2, 3, 4, 2])
        n = Node(8)
        l1.insert(None, n)
        self.check_list_consistency(l1)
        self.assertTrue(l1.tail.prev is n)

    def test_insert_3(self):
        l1 = LinkedList2()
        n1 = Node(1)
        n2 = Node(2)
        n3 = Node(3)
        l1.add_in_tail(n1)
        l1.add_in_tail(n2)
        l1.insert(n1, n3)

        self.check_list_consistency(l1)
        self.assertTrue(n1.next is n3)
        self.assertTrue(n2.prev is n3)

    def test_add_in_head(self):
        l1 = LinkedList2()
        n1 = Node(1)
        l1.add_in_head(n1)

        self.assertEqual(l1.len(), 1)
        self.check_list_consistency(l1)

        n2 = Node(2)
        l1.add_in_head(n2)

        self.assertEqual(l1.len(), 2)
        self.check_list_consistency(l1)
        self.assertTrue(n1.prev is n2)
        self.assertTrue(n2.next is n1)
