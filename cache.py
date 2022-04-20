class NativeCache:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size
        self.values = [None] * self.size
        self.hits = [0] * self.size

    def hash_fun(self, key):
        return sum(key.encode("utf-8")) % self.size

    def is_key(self, key):
        return key in self.slots

    def put(self, key, value):
        step = 3
        index = self.hash_fun(key)
        for i in range(self.size):
            if not self.slots[index] or self.slots[index] == key:
                self.slots[index] = key
                self.values[index] = value
                self.hits[index] += 1
                return

            index = (index + step) % self.size

        self.replace(key, value)

    def get(self, key):
        for i, val in enumerate(self.slots):
            if val == key:
                self.hits[i] += 1
                return self.values[i]

        return None

    def replace(self, key, value):
        target_index = self.hits.index(min(self.hits))
        self.slots[target_index] = key
        self.values[target_index] = value
        self.hits[target_index] = 1
