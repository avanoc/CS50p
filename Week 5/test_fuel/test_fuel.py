from fuel import convert
from fuel import gauge
import pytest

def main():
    test_notfraction()
    test_notint()
    test_zerodiv()
    test_empty()
    test_half()
    test_full()


def test_notfraction():
    with pytest.raises(ValueError):
        convert("34")


def test_notint():
    with pytest.raises(ValueError):
        convert("A/B")


def test_zerodiv():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_int():
    assert convert("3/4") == 75


def test_empty():
    assert gauge(1) == "E"


def test_half():
    assert gauge(75) == "75%"


def test_full():
    assert gauge(99) == "F"