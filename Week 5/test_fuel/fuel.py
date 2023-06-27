def main():
    while True:
        try:
            # Prompt the user to write a fraction
            fraction = input("Fraction: ")
            print(gauge(convert(fraction)))
        # Handle exceptions
        except (ValueError, ZeroDivisionError):
            pass


def convert(fraction):
    if "/" in fraction:
        fraction = fraction.split("/")

        # If the second number is zero, return corresponding error
        if fraction[1] == "0":
            raise ZeroDivisionError

        # If both numbers are not numbers, return corresponding error, or calculate %
        elif fraction[0].isnumeric() or fraction[1].isnumeric():
            percentage = round(int(fraction[0]) / int(fraction[1]) * 100)
            return int(percentage)
        else:
            raise ValueError
    else:
        raise ValueError


def gauge(n):
    # Return E for Empty
    if 0 <= n <= 1:
        return "E"

    # Return F for Full
    elif 99 <= n <= 100:
        return "F"

    # Return real percentage as a string
    elif 1 < n < 99:
        return str(n) + "%"


if __name__ == "__main__":
    main()