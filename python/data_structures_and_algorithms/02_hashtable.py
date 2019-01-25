import dataclasses


@dataclasses.dataclass
class Array:
    _size: int = 32
    init: None = None

    def __post_init__(self):
        self._items = [self.init] * self._size

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, index, value):
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item


@dataclasses.dataclass
class Slot:
    key: str or None
    value: object


class HashTable:
    UNUSED = None
    EMPTY = Slot(None, None)

    def __init__(self):
        self._table = Array(8, init=HashTable.UNUSED)
        self.length = 0

    @property
    def _load_factor(self):
        return (self.length / float(len(self._table))) >= 0.8

    def __len__(self):
        return self.length

    def _hash(self, key):
        return abs(hash(key)) % len(self._table)

    def _find_key(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while self._table[index] is not self.UNUSED:
            if self._table[index] is self.EMPTY:
                index = (index * 5 + 1) % _len
            elif key == self._table[index].key:
                return index
            else:
                index = (index * 5 + 1) % _len
        return None

    def _find_slot_for_insert(self, key):
        index = self._hash(key)
        _len = len(self._table)
        while not self._slot_can_insert(index):
            index = (index * 5 + 1) % _len
        return index

    def _slot_can_insert(self, index):
        return any((self._table[index] is self.EMPTY, self._table[index] is self.UNUSED))

    def __contains__(self, key):
        return self._find_key(key) is not None

    def add(self, key, value):
        if key in self:
            index = self._find_key(key)
            self._table[index].value = value
            return False
        else:
            index = self._find_slot_for_insert(key)
            self._table[index] = Slot(key, value)
            self.length += 1
            if self._load_factor:
                self._rehash()
            return True

    def _rehash(self):
        old_table = self._table
        self._table = Array(len(old_table) * 2, self.UNUSED)
        self.length = 0
        for slot in old_table:
            if slot is not self.UNUSED and slot is not self.EMPTY:
                index = self._find_slot_for_insert(slot.key)
                self._table[index] = slot
                self.length += 1

    def get(self, key, default=None):
        index = self._find_key(key)
        if index is None:
            return default
        return self._table[index].value

    def remove(self, key):
        index = self._find_key(key)
        if index is None:
            raise KeyError()
        value = self._table[index].value
        self._table[index] = self.EMPTY
        self.length -= 1
        return value

    def __iter__(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot.key


class DictADT(HashTable):

    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not  in self:
            raise KeyError()
        return self.get(key)

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashTable.EMPTY, HashTable.UNUSED):
                yield slot

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


class SetADT(HashTable):
    def add(self, key):
        return super().add(key, 1)

    def __add__(self, other):
        if isinstance(other, self.__class__):
            raise AttributeError()


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.get(i) == i

    assert sorted(list(d.keys())) == sorted(l)


def test_hash_table():
    h = HashTable()
    h.add('a', 0)
    h.add('b', 1)
    h.add('c', 2)
    assert len(h) == 3
    assert h.get('a') == 0
    assert h.get('b') == 1
    assert h.get('hehe') is None

    h.remove('a')
    assert h.get('a') is None
    assert sorted(list(h)) == ['b', 'c']

    n = 50
    for i in range(n):
        h.add(i, i)

    for i in range(n):
        assert h.get(i) == i


if __name__ == '__main__':
    print(
        'beg',
        test_hash_table(),
        'end',
    )
    test_dict_adt()
