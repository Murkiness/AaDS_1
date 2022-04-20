import pytest

from cache import NativeCache


def test_put():
    nc = NativeCache(17)
    nc.put("heh", "val")

    assert nc.hits[3] == 1
    assert nc.slots[3] == "heh"
    assert nc.values[3] == "val"


def test_put_overflow():
    nc = NativeCache(17)
    for i in range(18):
        nc.put(str(i), i)

    assert nc.hits[0] == 1
    assert nc.slots[0] == "17"
    assert nc.values[0] == 17


def test_put_overflow_2():
    nc = NativeCache(17)
    for i in range(18):
        nc.put(str(i), i)
        for j in range(i):
            nc.get(str(i))

    assert nc.hits[14] == 18
    assert nc.slots[14] == "17"
    assert nc.values[14] == 17
