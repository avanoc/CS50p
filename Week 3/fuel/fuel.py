def main():
    print(transformation("Fraction: "))


# Define a function that transforms the fraction to percentage value
def transformation(prompt):
    while True:
        try:
            # Prompt the user to write a fraction, split it into both numbers and calculate the corresponding %
            fraction = input(prompt).split("/")
            percentage = round(int(fraction[0]) / int(fraction[1]) * 100)

            # Return correct value
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            elif 1 < percentage < 99:
                return str(percentage) + "%"

        # Handle exceptions
        except (ValueError, ZeroDivisionError):
            pass

main()