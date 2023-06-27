from numb3rs import validate
import pytest

def main():
    test_numb3rs_4correct()
    test_numb3rs_4incorrect()
    test_numb3rs_some_correct()
    test_numb3rs_string()


def test_numb3rs_4correct():
    assert validate("255.255.255.255") == True


def test_numb3rs_4incorrect():
    assert validate("512.512.512.512") == False


def test_numb3rs_some_correct():
    assert validate("1.256.256.256") == False
    assert validate("1.1.256.256") == False
    assert validate("1.1.1.256") == False
    assert validate("1.256.1.1") == False
    assert validate("1.256.256.1") == False
    assert validate("1.256.1.256") == False
    assert validate("1.1.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("256.256.1.1") == False
    assert validate("256.256.256.1") == False
    assert validate("1.1.1.256") == False
    assert validate("256.1.256.1") == False
    assert validate("256.1.256.256") == False
    assert validate("256.1.1.256") == False


def test_numb3rs_string():
    assert validate("cat") == False


if __name__ == "__main__":
    main()