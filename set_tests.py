import pytest
import time

from set import PowerSet


def check_elements_in_set(ps, elements):
    for l in elements:
        assert ps.get(l) is True


def put_elements_in_set(ps, elements):
    for l in elements:
        ps.put(l)

def test_put():
    s = PowerSet()
    s.put("seve")
    assert "seve" in s.storage


def test_size():
    s = PowerSet()
    assert s.size() == 0
    s.put("1")
    s.put("1")
    s.put("1")
    assert s.size() == 1

    s.put("2")
    s.put("3")
    assert s.size() == 3


def test_get():
    s = PowerSet()
    assert s.get("23") is False
    s.put("23")
    assert s.get("23") is True


def test_remove():
    s = PowerSet()
    assert s.remove("hop") is False
    s.put("wot")
    assert s.remove("wot") is True
    assert s.remove("wot") is False


def test_intersection():
    s1 = PowerSet()
    s2 = PowerSet()

    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["b", "c", "d"])

    s3 = s1.intersection(s2)
    assert s3.get("b") is True
    assert s3.get("c") is True

    check_elements_in_set(s1, ["a", "b", "c"])
    check_elements_in_set(s2, ["b", "c", "d"])


def test_union():
    s1 = PowerSet()
    s2 = PowerSet()

    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["b", "c", "d"])

    s3 = s1.union(s2)

    for l in ["a", "b", "c", "d"]:
        assert s3.get(l) is True

    check_elements_in_set(s1, ["a", "b", "c"])
    check_elements_in_set(s2, ["b", "c", "d"])


def test_difference():
    s1 = PowerSet()
    s2 = PowerSet()

    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["b", "c", "d"])

    s3 = s1.difference(s2)
    s4 = s2.difference(s1)

    assert s3.get("a") is True
    assert s3.get("b") is False
    assert s3.get("c") is False

    assert s4.get("d") is True
    assert s4.get("b") is False
    assert s4.get("c") is False

    check_elements_in_set(s1, ["a", "b", "c"])
    check_elements_in_set(s2, ["b", "c", "d"])


def test_issubset_not_subset():
    s1 = PowerSet()
    s2 = PowerSet()
    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["b", "c", "d"])

    assert s1.issubset(s2) is False


def test_issubset_true():
    s1 = PowerSet()
    s2 = PowerSet()
    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["b", "c"])

    assert s1.issubset(s2) is True
    assert s2.issubset(s1) is False


def test_issubset_equal_sets():
    s1 = PowerSet()
    s2 = PowerSet()
    put_elements_in_set(s1, ["a", "b", "c"])
    put_elements_in_set(s2, ["a", "b", "c"])

    assert s1.issubset(s2) is True
    assert s2.issubset(s1) is True


def test_big_set_performance_get():
    s1 = PowerSet()
    elements = range(20000)
    put_elements_in_set(s1, elements)

    start = time.perf_counter_ns()
    assert s1.get(19988) is True
    assert s1.get(2000202) is False

    res_time = (time.perf_counter_ns() - start) / 1000
    assert 10 ** 6 > res_time


def test_big_set_performance_union():
    s1 = PowerSet()
    elements1 = range(20000)
    put_elements_in_set(s1, elements1)

    s2 = PowerSet()
    elements2 = range(10000, 30000)
    put_elements_in_set(s2, elements2)

    start = time.perf_counter_ns()
    res = s1.union(s2)
    res_time = (time.perf_counter_ns() - start) / 1000
    assert 10 ** 6 > res_time

    for i in range(10000, 19999):
        assert res.get(i) is True
