class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class OrderedList:
    def __init__(self, asc):
        self.head = None
        self.tail = None
        self.__ascending = asc

    def compare(self, v1, v2):
        if not self.__ascending:
            v1, v2 = v2, v1

        if v1 < v2:
            return -1
        if v2 < v1:
            return 1

        return 0

    def get_all(self):
        r = []
        node = self.head
        while node != None:
            r.append(node)
            node = node.next
        return r

    def add(self, value):
        n = Node(value)
        if self.head is None or self.compare(value, self.head.value) < 0:
            self.add_in_head(n)
            return

        if self.compare(value, self.tail.value) > 0:
            self.add_in_tail(n)
            return

        self.add_in_middle(n)

    def find(self, val):
        current = self.head

        while current is not None:
            if self.compare(current.value, val) == 0:
                return current

            current = current.next

        return None

    def delete(self, val, all=False):
        node = self.head
        prevNode = None

        while node is not None:
            if node.value == val:
                self._delete_node(node, prevNode)
                return
            else:
                prevNode = node
            node = node.next

    def clean(self, asc):
        self.__ascending = asc
        self.head = None
        self.tail = None

    def len(self):
        list_len = 0
        node = self.head

        while node is not None:
            list_len += 1
            node = node.next

        return list_len

    def _delete_node(self, node, prevNode):
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

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def add_in_head(self, item):
        item.next = self.head
        self.head = item
        if item.next is None:
            self.tail = item
        else:
            item.next.prev = item

    def add_in_middle(self, item):
        current = self.head.next
        prev = self.head

        while current is not None:
            if self.compare(item.value, current.value) < 0:
                break

            prev, current = current, current.next

        prev.next, current.prev = item, item
        item.prev, item.next = prev, current


class OrderedStringList(OrderedList):
    def __init__(self, asc):
        super(OrderedStringList, self).__init__(asc)

    def compare(self, v1, v2):
        v1s = v1.strip()
        v2s = v2.strip()

        if not self._OrderedList__ascending:
            v1s, v2s = v2s, v1s

        if v1s < v2s:
            return -1
        if v2s < v1s:
            return 1

        return 0
