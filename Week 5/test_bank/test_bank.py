from bank import value

def main():
    test_value_starts_hello()
    test_value_starts_h()
    test_value_otherwise()


def test_value_starts_hello():
    assert value("Hello customer") == 0


def test_value_starts_h():
    assert value("Hi customer") == 20


def test_value_otherwise():
    assert value("Welcome customer") == 100


if __name__ == "__main__":
    main()