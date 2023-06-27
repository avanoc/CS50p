import sys
from tabulate import tabulate
import csv

def main():
    if check():
        print(table())


def check():
    length = len(sys.argv)
    # Check the command-line arguments
    if length < 2:
        sys.exit("Too few command-line arguments")
    elif length > 2:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        return True

def table():
    # Define a list where to append information
    data = []

    # Open CSV file
    try:
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for row in reader:
                data.append({"pizza": row[0], "small": row[1], "large": row[2]})

            # Return the tabulated list, formatted as a grid
            return tabulate(data, headers="firstrow", tablefmt = "grid")

    # Handle non existing file
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()