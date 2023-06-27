from twttr import shorten

def main():
    test_shorten()


def test_shorten():
    assert shorten("HellO World! 12345") == "Hll Wrld! 12345"


if __name__ == "__main__":
    main()