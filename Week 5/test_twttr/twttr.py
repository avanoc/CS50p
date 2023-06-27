def main():
    # Prompt user for some text
    text = input("Input: ")

    # Print the same text without the vowels
    print("Output: ", shorten(text))


def shorten(text):
    # Initialize a list where to save all letters from original text
    output = []

    # Loop through the text to retrieve all characters
    for letter in text:

        # If the character is not a vowel, append it to the list
        if not is_vowel(letter):
            output.append(letter)

    # Return the list as a string
    return "".join(output)


def is_vowel(char):
    # Define a vowel
    vowel = ["a", "e", "i", "o", "u"]

    # If the given character, in lowercase, is a vowel, return "True"
    if char.lower() in vowel:
        return True


if __name__ == "__main__":
    main()