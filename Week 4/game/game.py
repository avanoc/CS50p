import random


def main():
    number, level = get_level()
    check_guess(number, level)


def get_level():
    while True:

        # Get positive integer from user
        try:
            level = int(input("Level: "))
            if level < 0:
                continue

            # Select a random number between 0 and the number chosen by the user
            random_number = random.randint(0, level)

        # If not, prompt again
        except (NameError, ValueError):
            continue

        # End loop
        break
    return random_number, level


def check_guess(r, l):
    while True:
        # Ask the user to guess the number selected randomly
        try:
            guess = int(input("Guess: "))
            if 0 > guess > l:
                continue

            # Check if the number guessed is correct, pass until it is, then break
            if guess < r:
                print("Too small!")
                pass

            elif guess > r:
                print("Too large!")
                pass

            else:
                print("Just right!")
                break

        # If number is not a positive integer, ask again
        except (NameError, ValueError):
            continue

if __name__ == "__main__":
    main()