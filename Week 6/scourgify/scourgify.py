import sys
import csv

def main():
    if check():
        convert()

def check():

    # Check correct command-line arguments
    length = len(sys.argv)
    if length < 3:
        sys.exit("Too few command-line arguments")
    elif length > 3:
        sys.exit("Too many command-line arguments")
    elif ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")
    else:
        return True

def convert():
    # Create a list
    converted = []

    # Open CSV file to be formatted
    try:
        with open(sys.argv[1]) as before:
            reader = csv.DictReader(before)
            for row in reader:

                # Separate name into first and last name
                last, first = row["name"].split(",")

                # Append formatted row to a list
                converted.append({"first": first.strip(), "last": last, "house": row["house"]})

    # Handle exception if file doesn't exist
    except FileNotFoundError:
        sys.exit(f"Could not read {argv[1]}")

    # Create a new CSV file
    with open(sys.argv[2], "w") as after:
        writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])

        # Include a header, with the fieldanmes that where set for writer
        writer.writeheader()

        # Write each row in the CSV file
        for row in converted:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})


if __name__ == "__main__":
    main()