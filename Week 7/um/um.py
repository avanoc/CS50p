import re

def main():
    print(count(input("Text: ")))


def count(s):

    # Set counter to zero
    counter = 0

    # Split the user's input into each word
    split = s.split(" ")

    # Iterate through user's input to find "um", and add 1 to counter for each "um" found
    for word in split:
        if re.search(r"^um\W+?", word, re.IGNORECASE):
            counter = counter + 1

    # Return the final count
    return counter


if __name__ == "__main__":
    main()