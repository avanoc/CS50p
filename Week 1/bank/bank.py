def main():
    # Prompt user for a greeting:
    greeting = input("Greeting: ")

    # Print the amount due:
    print(f"$ {value(greeting)}")


def value(greeting):
    # Dismiss whitespaces and convert the string to lowercase
    greeting = greeting.strip().lower()

    # Check if any amount is due, based on the greeting:
    if "hello" in greeting.split(" ", 1)[0]:
        return 0
    elif greeting[0] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()