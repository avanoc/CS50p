import sys

def main():
    if check():
        print(counter())


def counter():
    # Set counter to zero
    i = 0

    # Count lines
    try:
        with open(sys.argv[1]) as file:
            for line in file:
                if line.replace(" ", "")[0] not in ("\n", "#"):
                    i = i + 1
            return i

    # If file doesn't exist
    except FileNotFoundError:
        sys.exit("File does not exist")

def check():
    # Define length of command-line arguments
    length = len(sys.argv)

    # Check correct implementation of command-line arguments
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    elif ".py" not in sys.argv[1]:
        sys.exit("Not a python file")
    else:
        return True

if __name__ == "__main__":
    main()