# Stack where top is the head
class Stack:
    def __init__(self):
        self.stack = LinkedList2()

    def size(self):
        return self.stack.len()

    def pop(self):
        return self.stack.pop_value_from_top(False)

    def push(self, value):
        n = Node(value)
        self.stack.add_in_head(n)

    def peek(self):
        return self.stack.get_value_from_top(False)


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

    def len(self):
        list_len = 0
        node = self.head

        while node is not None:
            list_len += 1
            node = node.next

        return list_len

    def add_in_head(self, newNode):
        newNode.next = self.head
        self.head = newNode
        if newNode.next is None:
            self.tail = newNode
        else:
            newNode.next.prev = newNode

    def get_value_from_top(self, tail=True):
        if self.tail is None:
            return None

        if tail:
            return self.tail.value
        return self.head.value

    def pop_value_from_top(self, tail=True):
        val = None
        if tail and self.tail:
            val = self.tail.value
            if self.tail.prev:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.tail = self.head = None
        if not tail and self.head:
            val = self.head.value
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = self.tail = None

        return val
