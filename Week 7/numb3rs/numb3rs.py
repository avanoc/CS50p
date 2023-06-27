import re


def main():
    # Prompt user for an IPv4 Address. Check if the return value after Validate is True or False
    if validate(input("IPv4 Address: ")):
        print("True")
    else:
        print("False")


def validate(ip):

    # Try to split input using dots
    try:
        first,second,third,fourth = ip.split(".")

    # if no dots exist, return False
    except ValueError:
        return False

    # Place the returned values of spliting the input into a list
    numbers = [first, second, third, fourth]

    # Set a counter to zero
    validation = 0

    # Iterate through the list and check the values. If the RE is met, then update the counter
    for number in numbers:
        if number < "256":
            if re.search(r"^[0-2]?[0-5]?\d$", number):
                validation = validation + 1

    # If the counter is updated 4 times, return True, else False
    if validation == 4:
        return True
    else:
        return False


if __name__ == "__main__":
    main()