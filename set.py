class PowerSet:

    def __init__(self):
        self.storage = {}

    def size(self):
        return len(self.storage.keys())

    def put(self, value):
        self.storage[value] = True

    def get(self, value):
        return bool(self.storage.get(value, None))

    def remove(self, value):
        return bool(self.storage.pop(value, None))

    def intersection(self, set2):
        res = PowerSet()
        for k in self.storage:
            if set2.get(k):
                res.put(k)

        return res

    def union(self, set2):
        res = PowerSet()
        for k in self.storage:
            res.put(k)

        for k in set2.storage:
            res.put(k)

        return res

    def difference(self, set2):
        res = PowerSet()
        for k in self.storage:
            if not set2.get(k):
                res.put(k)

        return res

    def issubset(self, set2):
        for k in self.storage:
            if not set2.get(k):
                return False

        return True
