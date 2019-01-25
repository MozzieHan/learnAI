

class EmptyValueClass:
    def __str__(self):
        return "empty value"

    def __repr__(self):
        return "empty value"


class DummyValueClass:
    def __str__(self):
        return "dummy value"

    def __repr__(self):
        return "dummy value"


EMPTY = EmptyValueClass()
DUMMY = DummyValueClass()


class Slot:
    def __init__(self, hash_code=EMPTY, key=EMPTY, value=EMPTY):
        self.hash_code = hash_code
        self.key = key
        self.value = value

    def __str__(self):
        return "key: {}, value: {}  ".format(self.key, self.value)

    def __repr__(self):
        return "key: {}, value: {}  ".format(self.key, self.value)


class AlmostDict:
    def __init__(self, pairs=None):
        self.slots = [Slot() for _ in range(8)]
        self.fill = 0
        self.used = 0
        if pairs:
            for k, v in pairs:
                self[k] = v

    def __getitem__(self, key):
        hash_code = hash(key)
        idx = hash_code % len(self.slots)
        while self.slots[idx].key is not EMPTY:
            if self.slots[idx].hash_code == hash_code and self.slots[idx].key == key:

                return self.slots[idx].value
            idx = (idx + 1) % len(self.slots)
        raise KeyError(key)

    def __setitem__(self, key, value):
        hash_code = hash(key)
        idx = hash_code % len(self.slots)
        while self.slots[idx].key is not EMPTY:
            if self.slots[idx].hash_code == hash_code and self.slots[idx].key == key:
                break
            idx = (idx + 1) % len(self.slots)

        if self.slots[idx].key is EMPTY:
            self.fill += 1
            self.used += 1
        self.slots[idx] = Slot(hash_code, key, value)
        if self.fill * 3 >= len(self.slots) * 2:
            self.resize()

    def __delitem__(self, key):
        pass

    def find_closest_size(self, minused):
        new_size = 8
        while new_size <= minused:
            new_size *= 2
        return new_size

    def resize(self):
        old_slots = self.slots
        new_size = self.find_closest_size(self.used * 2)
        self.slots = [Slot() for _ in range(new_size)]
        self.fill = self.used
        for slot in old_slots:
            if slot.key is not EMPTY and slot.key is not DUMMY:
                idx = slot.hash_code % len(self.slots)
                while self.slots[idx].key is not EMPTY:
                    idx = (idx + 1) % len(self.slots)
                self.slots[idx] = slot


if __name__ == '__main__':
    a = AlmostDict((
        ("a", 1), ("b", 2), ("c", 3),
        ("a1", 1), ("b1", 2), ("c1", 3),
        ("a2", 1), ("b2", 2), ("c2", 3),
        ("a3", 1), ("b3", 2), ("c3", 3),
    ))
    print(a["a"])
    print(a["b1"])
    print(a["c3"])
    print(a["d"])

