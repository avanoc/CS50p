import seasons
import pytest


def main():
    test_format1()
    test_format2()
    test_format3()


def test_format1():
    with pytest.raises(SystemExit, match="Invalid date") as Error:
        seasons.get_dob("21 October 1982")
    assert Error.type == SystemExit


def test_format2():
    with pytest.raises(SystemExit, match="Invalid date") as Error:
        seasons.get_dob("21-10-1982")
    assert Error.type == SystemExit


def test_format3():
    with pytest.raises(SystemExit, match="Invalid date") as Error:
        seasons.get_dob("10-21-1982")
    assert Error.type == SystemExit


if __name__ == "__main__":
    main()