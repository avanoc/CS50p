def main():
    text = input("Input: ")
    no_vowels(text)


def no_vowels(text):
    print("Output: ", end = "")
    for letter in text:
        if is_vowel(letter):
            letter = ""
        print(letter, end = "")
    print()


def is_vowel(char):
    vowel = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    if char in vowel:
        return True


main()