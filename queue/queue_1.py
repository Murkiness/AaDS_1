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

    def pop_value_from_top(self, tail=True):
        if tail and self.tail:
            return self._tail_pop()
        if not tail and self.head:
            return self._head_pop()

        return None

    def _tail_pop(self):
        val = self.tail.value
        if self.tail.prev:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            self.tail = self.head = None

        return val

    def _head_pop(self):
        val = self.head.value
        if self.head.next:
            self.head = self.head.next
            self.head.prev = None
        else:
            self.head = self.tail = None

        return val


class Queue:
    def __init__(self):
        self.queue = LinkedList2()

    def enqueue(self, item):
        n = Node(item)
        self.queue.add_in_tail(n)

    def dequeue(self):
        return self.queue.pop_value_from_top(False)

    def size(self):
        return self.queue.len()
