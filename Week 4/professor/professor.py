import random
import collections


def main():
    # Prompt user for a level
    level = get_level()

    # Initialize variables
    tries = 3
    i = 1
    score = 0

    # Get 10 ecuations
    while i <= 10:
        x = generate_integer(level)
        y = generate_integer(level)

        # Calculate correct answer
        correct = x + y

        # Present the ecuation to the user, until the user answers correctly
        question = (f"{x} + {y} = ")
        while True:
            print(question, end = "")
            answer = input()
            if answer != str(correct):
                print("EEE")

                # If user doesn't get it right the third time, show the answer
                tries = tries - 1
                if tries == 0:
                    print(f"{question}{correct}")
                    i = i + 1
                    break
                else:
                    continue

            # When user does the math right, update variables and reset tries
            else:
                tries = 3
                i = i + 1
                score = score + 1
                break

    # Show final score
    print(f"Score: {score}")


def get_level():
    # Initiate level at 0
    level = 0

    # Prompt user for a level, until level is 1, 2 or 3
    while level not in ["1", "2", "3"]:
        level = input("Level: ")

    return int(level)

def generate_integer(level):
    # Set lower and upper limits
    first = "".join(collections.OrderedDict.fromkeys("1" * (level - 1)))
    second = "0" * (level - 1)
    lower = int((f"{first or 0}{second}"))
    upper = 10 ** level - 1

    # Get a random non-negative integer
    while True:
        try:
            n = random.randint(lower, upper)
            if n < 0:
                raise ValueError

        except ValueError:
            continue

        return n


if __name__ == "__main__":
    main()