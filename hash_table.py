class HashTable:

    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):
        return sum(value.encode("utf-8")) % self.size

    def find(self, value):
        return self._gen_seek(value, self._find_cond_func)

    def seek_slot(self, value):
        return self._gen_seek(value, self._seek_slot_func)

    def put(self, value):
        index = self.seek_slot(value)
        if index is None:
            return None

        self.slots[index] = value
        return index

    def _gen_seek(self, value, cond_func):
        tries = set()

        index = self.hash_fun(value)
        while True:
            if cond_func(index, value):
                return index

            tries.add(index)

            if len(tries) == self.size:
                return None

            index = (index + self.step) % self.size

    def _find_cond_func(self, index, value):
        return self.slots[index] == value

    def _seek_slot_func(self, index, value):
        return self.slots[index] is None
