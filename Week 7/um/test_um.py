from um import count

def main():
    test_correct()
    test_nocount()
    test_similar()


def test_correct():
    assert count("Um, hello... um... world") == 2


def test_nocount():
    assert count("Hello, world") == 0


def test_similar():
    assert count("thanks for the album.") == 0


if __name__ == "__main__":
    main()