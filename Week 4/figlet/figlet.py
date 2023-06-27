import pyfiglet
import sys

# Define that the 3rd argument shall be called "font"
font = sys.argv[2]

def main():
    # Result if user doesn't want to style the text
    if len(sys.argv) == 1:
        prompt()
        print(format(text))

    # Result if user wants to style the text from command-line
    # Check that user has input the correct commands
    elif len(sys.argv) == 3 and sys.argv[1] == ("-f" or "--font"):

        # Check that user has input an existing font
        format("a")

        # Prompt user for text and format text as requested
        text = prompt()
        print(format(text))

    else:
        invalid()

# Create a function to prompt user for input
def prompt():
    return input("Input: ")


# Create a function to format the text
def format(n):
    try:
        formated = pyfiglet.figlet_format(n, font)
        return(formated)
    except:
        invalid()


# Create a function to exit with error message
def invalid():
    sys.exit("Invalid usage")


if __name__ == "__main__":
    main()