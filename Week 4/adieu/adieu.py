names = []

def main():
    while True:
        try:
            names.append(input("Name: "))

        # Stop trying whit ctrl-d
        except EOFError:

            # Print message in a new line
            print()

            # Print first part of message
            print(f"Adieu, adieu, to ", end = "")
            all_names()

            # End program
            break


def all_names():
    # If only 1 name has been entered
    if len(names) == 1:
        print(names[0])

    # If 2 names have been entered
    elif len(names) == 2:
        print(f"{names[0]} and {names[1]}")

    # If 3 or more names have been entered
    else:
        for name in names[:-1]:
            print(name, end = ", ")
        print(f"and {names[-1]}")


if __name__ == "__main__":
    main()