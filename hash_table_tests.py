import pytest

from hash_table import HashTable


@pytest.mark.parametrize('value, index', [
    ('abc', 5),
    ('abcd', 3),
    ('хаба хаба', 13),
    ('z675zu arf45309!&', 10),
    ('  z675zu  arf45309!&  ', 0)
])
def test_hash_func(value, index):
    ht = HashTable(17, 2)
    assert ht.hash_fun(value) == index


@pytest.mark.parametrize('value, index', [
    ('abc', 5),
    ('abcd', 3),
    ('хаба хаба', 13),
    ('z675zu arf45309!&', 10),
    ('  z675zu  arf45309!&  ', 0)
])
def test_seek_slot(value, index):
    ht = HashTable(17, 2)
    assert ht.seek_slot(value) == index


def test_seek_slot_when_filled():
    ht = HashTable(7, 2)
    assert ht.hash_fun("zda") == ht.hash_fun("zzK")
    ht.put("zda")
    assert ht.seek_slot("zzK") == 6


def test_seek_slot_when_hash_table_full():
    ht = HashTable(7, 2)
    for i in range(7):
        ht.put(str(i))

    assert ht.seek_slot("7") is None

@pytest.mark.parametrize('value, index', [
    ('abc', 5),
    ('abcd', 3),
    ('хаба хаба', 13),
    ('z675zu arf45309!&', 10),
    ('  z675zu  arf45309!&  ', 0)
])
def test_put(value, index):
    ht = HashTable(17, 2)
    ht.put(value)

    assert ht.slots[index] == value


def test_put_when_hash_table_full():
    ht = HashTable(7, 2)
    for i in range(7):
        ht.put(str(i))

    assert ht.put("7") is None


@pytest.mark.parametrize('value, index', [
    ('abc', 5),
    ('abcd', 3),
    ('хаба хаба', 13),
    ('z675zu arf45309!&', 10),
    ('  z675zu  arf45309!&  ', 0)
])
def test_find(value, index):
    ht = HashTable(17, 2)
    ht.put(value)
    assert ht.find(value) == index


def test_find_non_existent():
    ht = HashTable(17, 2)
    assert ht.find("heh") is None


def test_find_in_full_hash_table():
    ht = HashTable(7, 2)
    for i in range(7):
        ht.put(str(i))

    assert ht.find("8") is None
    assert ht.find("6") == 5
