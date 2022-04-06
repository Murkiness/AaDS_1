class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head

        while node is not None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head

        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found = []
        node = self.head

        while node is not None:
            if node.value == val:
                found.append(node)
            node = node.next

        return found

    def delete(self, val, all=False):
        node = self.head
        prevNode = None

        while node is not None:
            if node.value == val:
                self.delete_node(node, prevNode)
                if not all:
                    break
            prevNode = node
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head

        while node is not None:
            list_len += 1
            node = node.next

        return list_len

    def insert(self, afterNode, newNode):
        node = self.head
        if afterNode is None and node is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None:
            self.head = newNode
            newNode.next = node
        else:
            while node is not None:
                if node is afterNode:
                    nextNode = node.next
                    node.next = newNode
                    newNode.next = nextNode
                    if nextNode is None:
                        self.tail = newNode
                    break
                node = node.next

    def delete_node(self, node, prevNode):
        if node is self.head:
            self.head = node.next
        elif node is self.tail:
            self.tail = prevNode
            self.tail.next = None
        else:
            prevNode.next = node.next

    def get_list_as_array(self):
        array = []

        if self.head is None:
            return None

        node = self.head
        while node is not None:
            array.append(node.value)
            node = node.next

        return array


def sum_lists(list1, list2):
    l1_node = list1.head
    l2_node = list2.head

    if l1_node is None or l2_node is None:
        return None

    res_list = LinkedList()
    res_list.head = Node(l1_node.value + l2_node.value)

    l1n = l1_node.next
    l2n = l2_node.next

    current_node = res_list.head

    while l1n and l2n:
        newNode = Node(l1n.value + l2n.value)
        current_node.next = newNode
        current_node = newNode
        l1n = l1n.next
        l2n = l2n.next

    # if something is not None, then list lengths are not equal
    if l1n or l2n:
        return None

    res_list.tail = current_node

    return res_list
