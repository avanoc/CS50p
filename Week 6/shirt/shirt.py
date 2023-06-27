import sys
from PIL import (Image, ImageOps)

def main():
    if check():
        overlay()


def check():
    # Check for correct command-line arguments
    length = len(sys.argv)
    extensions = ["png", "jpeg", "jpg"]

    try:
        # Retrieve extension from files
        extension_input = sys.argv[1].lower().split(".")
        extension_output = sys.argv[2].lower().split(".")

        if length < 3:
            sys.exit("Too few command-line arguments")
        elif length > 3:
            sys.exit("Too many command-line arguments")
        elif (extension_input[1] and extension_output[1]) not in extensions:
            sys.exit("Invalid input")
        elif extension_input[1] != extension_output[1]:
            sys.exit("Input and Output have different extensions")
        else:
            return True

    # Handle error if files have no extensions
    except IndexError:
        sys.exit("Invalid input")


def overlay():
    # Retrieve input and output names from command-line arguments
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    shirt = Image.open("shirt.png")
    size = shirt.size

    try:
        # Open original image and format it to fit the shirt
        original = Image.open(input_image, mode='r', formats=None)

    # Handle exceptions that may raise
    except (FileNotFoundError):
        sys.exit("Invalid input")

    # Overlay shirt to original image, and save output:
    original = ImageOps.fit(original, size)
    original.paste(shirt, shirt)
    original.save(output_image)


if __name__ == "__main__":
    main()