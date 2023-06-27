def main():
    name = input("camelCase: ")
    snake_case(name)


def snake_case(name):
    print("snake_case: ", end = "")
    for letter in name:
        if letter.islower():
            print(letter, end = "")
        elif letter.isupper():
            print("_" + letter.lower(), end = "")
    print()

main()