# two stack implementation
class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if len(self.stack2) == 0:
            self._refill_stack2()

        if len(self.stack2) == 0:
            return None
        return self.stack2.pop()

    def size(self):
        return len(self.stack1) + len(self.stack2)

    def _refill_stack2(self):
        while len(self.stack1) != 0:
            self.stack2.append(self.stack1.pop())