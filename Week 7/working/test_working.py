import pytest
from working import convert

def main():
    test_to()
    test_colon()
    test_minutes()
    test_hours()
    test_no_to()


# Test that "to" is accepted
def test_to():
    assert convert("5 AM to 9 PM") == "05:00 to 21:00"


# Test that if there's a colon in the format, it will be correctly converted
def test_colon():
    assert convert("5:00 AM to 9:00 PM") == "05:00 to 21:00"


# Test that invalid minutes will raise a ValueError
def test_minutes():
    with pytest.raises(ValueError):
        convert("5:60 AM to 9:00 PM")


# Test that invalid format of hours will raise a ValueError
def test_hours():
    with pytest.raises(ValueError):
        convert("17 to 9")


# Test that omitting a "to" between hours will raise a ValueError
def test_no_to():
    with pytest.raises(ValueError):
        convert("5 AM - 21 PM")