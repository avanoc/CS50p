def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check plate's length
    if 2 <= len(s) <= 6:

        # Set base value for letters
        i = 0
        for c in s:

            # Check if plate first and second characters are letters in uppercase
            if c.isalpha() and i == 0:
                continue

            # Check if some characters are numbers
            elif c.isnumeric():

                # Check that first number is not 0
                if i == 0 and int(c) == 0:
                    return False

                # Set value for numbers
                elif i == 0:
                    i = 1
                    continue

                else:
                    continue

            # If none of the conditions above are met, return False
            else:
                return False

        # If all of the conditions above are met, return True
        return True

    # If plate length is not between 2 and 6 characters, return False
    else:
        return False


if __name__ == "__main__":
    main()