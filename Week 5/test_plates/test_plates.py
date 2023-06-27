from plates import is_valid

def main():
    test_length()
    test_numbers_first()
    test_zero_first()
    test_nonalpha()
    test_number_placement()


def test_length():
    assert is_valid("C") == False
    assert is_valid("HTRCS50") == False


def test_numbers_first():
    assert is_valid("00") == False
    assert is_valid("10") == False


def test_zero_first():
    assert is_valid("LUV00") == False
    assert is_valid("LUV10") == True


def test_nonalpha():
    assert is_valid("@LUV1") == False
    assert is_valid("LUV@1") == False
    assert is_valid("LUV1@") == False


def test_number_placement():
    assert is_valid("CS50HI") == False


if __name__ == "__main__":
    main()