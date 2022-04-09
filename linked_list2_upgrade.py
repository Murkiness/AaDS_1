class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class HiddenNode(Node):
    def __init__(self, v=None):
        super().__init__(v)


class LinkedList2:
    def __init__(self):
        self.head = HiddenNode()
        self.tail = HiddenNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_in_tail(self, item):
        prev = self.tail.prev
        self.tail.prev = item
        prev.next = item
        item.next = self.tail
        item.prev = prev

    def find(self, val):
        node = self.head.next

        while not isinstance(node, HiddenNode):
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found = []
        node = self.head.next

        while not isinstance(node, HiddenNode):
            if node.value == val:
                found.append(node)
            node = node.next

        return found

    def delete(self, val, all=False):
        node = self.head.next
        prevNode = self.head

        while not isinstance(node, HiddenNode):
            if node.value == val:
                self.delete_node(node, prevNode)
                if not all:
                    break
            else:
                prevNode = node
            node = node.next

    def clean(self):
        self.head.next = self.tail
        self.tail.prev = self.head

    def len(self):
        list_len = 0
        node = self.head.next

        while not isinstance(node, HiddenNode):
            list_len += 1
            node = node.next

        return list_len

    def insert(self, afterNode, newNode):
        if afterNode is None and self.len() == 0:
            self.add_in_head(newNode)
        elif afterNode is None and self.len() > 0:
            self.add_in_tail(newNode)
        else:
            node = self.head.next
            while not isinstance(node, HiddenNode):
                if node is afterNode:
                    newNode.next = node.next
                    newNode.prev = node
                    node.next = newNode
                    newNode.next.prev = newNode
                    break
                node = node.next

    def add_in_head(self, newNode):
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next.prev = newNode
        self.head.next = newNode

    def delete_node(self, node, prevNode):
        prevNode.next = node.next
        prevNode.next.prev = prevNode

    def value_list_from_head(self):
        res = []
        node = self.head.next

        while not isinstance(node, HiddenNode):
            res.append(node.value)
            node = node.next

        return res

    def value_list_from_tail(self):
        res = []
        node = self.tail.prev

        while not isinstance(node, HiddenNode):
            res.append(node.value)
            node = node.prev

        return res
