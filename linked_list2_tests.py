import unittest
from linked_list2 import LinkedList2, Node


class TestLinkedList2(unittest.TestCase):

    def build_list(self, array):
        list = LinkedList2()
        for el in array:
            list.add_in_tail(Node(el))

        return list

    def setUp(self):
        self.list = LinkedList2()
        self.n1 = Node(1)
        self.n2 = Node(2)
        self.n3 = Node(3)

        for n in [self.n1, self.n2, self.n3]:
            self.list.add_in_tail(n)

    def test_find_successfully(self):
        for i in [1, 2, 3]:
            with self.subTest(i=i):
                r = self.list.find(i)
                self.assertTrue(r is not None)
                self.assertTrue(r.value == i)

    def test_find_unsuccessfully(self):
        r = self.list.find(11)
        self.assertTrue(r is None)

    def test_find_all(self):
        add_n = Node(1)
        self.list.add_in_tail(add_n)

        res = self.list.find_all(1)
        self.assertTrue(len(res) == 2)
        self.assertTrue(res[0] is self.n1)
        self.assertTrue(res[1] is add_n)

        res1 = self.list.find_all(2)
        self.assertTrue(len(res1) == 1)
        self.assertTrue(res1[0] is self.n2)

        res2 = self.list.find_all(500)
        self.assertTrue(res2 == [])

    def test_delete_middle(self):
        self.list.delete(2)
        self.assertTrue(self.list.head is self.n1)
        self.assertTrue(self.list.tail is self.n3)
        self.assertTrue(self.list.find(2) is None)
        self.assertTrue(self.list.head.next is self.n3)
        self.assertTrue(self.list.tail.prev is self.n1)

    def test_delete_head(self):
        self.list.delete(1)
        self.assertTrue(self.list.head is self.n2)
        self.assertTrue(self.list.tail is self.n3)
        self.assertTrue(self.list.find(1) is None)
        self.assertTrue(self.list.head.prev is None)

    def test_delete_tail(self):
        self.list.delete(3)
        self.assertTrue(self.list.head is self.n1)
        self.assertTrue(self.list.tail is self.n2)
        self.assertTrue(self.list.find(3) is None)
        self.assertTrue(self.list.tail.next is None)

    def test_delete_all_mono(self):
        list = self.build_list([1, 1, 1, 1])
        list.delete(1, True)
        self.assertTrue(list.tail is None)
        self.assertTrue(list.head is None)

    def test_delete_all_except_tail(self):
        n = Node(2)
        list = self.build_list([1, 1, 1])
        list.add_in_tail(n)
        self.assertTrue(list.tail is n)
        self.assertTrue(n.prev.value == 1)
        self.assertTrue(n.next is None)
        list.delete(1, True)
        self.assertTrue(list.tail is n)
        self.assertTrue(list.head is n)
        self.assertTrue(n.prev is None)
        self.assertTrue(n.next is None)

    def test_delete_all_except_head(self):
        n = Node(2)
        list = self.build_list([1, 1, 1])
        list.add_in_head(n)
        self.assertTrue(list.head is n)
        self.assertTrue(n.next.value == 1)
        self.assertTrue(n.prev is None)
        list.delete(1, True)
        self.assertTrue(list.tail is n)
        self.assertTrue(list.head is n)
        self.assertTrue(n.prev is None)
        self.assertTrue(n.next is None)

    def test_delete_all_edges(self):
        list = self.build_list([1, 2, 2, 1])
        list.delete(1, True)
        self.assertTrue(list.tail.prev is list.head)
        self.assertTrue(list.tail.next is None)
        self.assertTrue(list.tail.value == 2)
        self.assertTrue(list.head.prev is None)
        self.assertTrue(list.head.next is list.tail)
        self.assertTrue(list.head.value == 2)

    def test_delete_all_middle(self):
        list = self.build_list([2, 1, 1, 2])
        list.delete(1, True)
        self.assertTrue(list.tail.prev is list.head)
        self.assertTrue(list.tail.next is None)
        self.assertTrue(list.tail.value == 2)
        self.assertTrue(list.head.prev is None)
        self.assertTrue(list.head.next is list.tail)
        self.assertTrue(list.head.value == 2)

    def test_clean(self):
        self.list.clean()
        self.assertTrue(self.list.head is None)
        self.assertTrue(self.list.tail is None)

    def test_len_no_elements(self):
        ll = LinkedList2()
        self.assertTrue(ll.len() == 0)

    def test_len_w_elements(self):
        self.assertTrue(self.list.len() == 3)

    def test_insert_w_none_empty_list(self):
        ll = LinkedList2()
        n = Node(1)
        ll.insert(None, n)
        self.assertTrue(ll.head is n)
        self.assertTrue(ll.tail is n)

    def test_insert_w_none_non_empty_list(self):
        n = Node(111)
        self.list.insert(None, n)
        self.assertTrue(self.list.tail is n)
        self.assertTrue(self.list.head is not n)
        self.assertTrue(self.list.head is self.n1)

    def test_insert_as_last(self):
        n = Node(111)
        self.list.insert(self.n3, n)
        self.assertTrue(self.list.tail is n)
        self.assertTrue(self.list.tail.prev is self.n3)
        self.assertTrue(self.list.tail.prev.next is n)

    def test_insert_middle(self):
        n = Node(111)
        self.list.insert(self.n2, n)
        self.assertTrue(self.list.tail is self.n3)
        self.assertTrue(self.list.head is self.n1)
        self.assertTrue(self.list.tail.prev is n)
        self.assertTrue(self.n2.next is n)

    def test_add_in_head_empty(self):
        list = LinkedList2()
        n = Node(5)
        list.add_in_head(n)
        self.assertTrue(list.head is n)
        self.assertTrue(list.tail is n)

    def test_add_in_head_non_empty(self):
        n = Node(7)
        self.list.add_in_head(n)
        self.assertTrue(self.list.head is n)
        self.assertTrue(self.n1.prev is n)
        self.assertTrue(self.list.head.prev is None)
        self.assertTrue(self.list.head.next.value == 1)
