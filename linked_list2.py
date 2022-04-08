class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

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
            else:
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
        if afterNode is None and self.head is None:
            self.head = newNode
            self.tail = newNode
        elif afterNode is None:
            newNode.prev = self.tail
            self.tail.next = newNode
            self.tail = newNode
        else:
            node = self.head
            while node is not None:
                if node is afterNode:
                    newNode.next = node.next
                    newNode.prev = node
                    node.next = newNode
                    if newNode.next is None:
                        self.tail = newNode
                    else:
                        newNode.next.prev = newNode
                    break
                node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head
        self.head = newNode
        if newNode.next is None:
            self.tail = newNode
        else:
            newNode.next.prev = newNode

    def delete_node(self, node, prevNode):
        if node is self.head and node is self.tail:
            self.head = None
            self.tail = None
        elif node is self.head:
            self.head = node.next
            self.head.prev = None
        elif node is self.tail:
            self.tail = prevNode
            self.tail.next = None
        else:
            prevNode.next = node.next
            prevNode.next.prev = prevNode

