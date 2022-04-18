import pytest

from dictionary import NativeDictionary


def test_put():
    d = NativeDictionary(17)
    d.put("hoba", "value")
    assert d.slots[2] == "hoba"
    assert d.values[2] == "value"


def test_put_same_value():
    d = NativeDictionary(17)
    d.put("hoba", "value")
    d.put("hoba", "value")
    assert d.slots[2] == "hoba"
    assert d.values[2] == "value"


def test_put_collision():
    d = NativeDictionary(17)
    d.put("erba", "value1")
    d.put("hoba", "value2")
    assert d.slots[2] == "erba"
    assert d.values[2] == "value1"
    assert d.slots[5] == "hoba"
    assert d.values[5] == "value2"


def test_put_exhaust_capacity():
    d = NativeDictionary(17)
    for i in range(18):
        d.put(str(i), i)

    for i in range(17):
        assert d.is_key(str(i)) is True

    assert d.is_key(str(18)) is False


def test_is_key():
    d = NativeDictionary(17)
    d.put("hoba", "value")
    assert d.is_key("hoba") is True
    assert d.is_key("value") is False


def test_get():
    d = NativeDictionary(17)
    d.put("hoba", "value")
    assert d.get("hoba") == "value"
    assert d.get("heh") is None
