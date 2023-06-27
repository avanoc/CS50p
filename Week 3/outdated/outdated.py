def main():
    convert("Date: ")


def convert(prompt):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input(prompt).strip()

            # Separate date into day, month and year, depending how it's been written
            if "/" in date:
                date = date.split("/")
                for d in date:
                    if d.isalpha():
                        raise ValueError
            elif "," in date:
                date = date.split(" ")
            else:
                raise ValueError

            # Retrieve year, month and date from date separated
            yyyy = date[2]
            mm = date[0]
            dd = date[1].replace(",", "")

            # Check if month has been introduced as a string
            if mm.isalpha():
                for month in months:
                    if mm == month:
                        mm = str(months.index(month) + 1)
                        break

            # Check that the year and the day are not strings
            elif yyyy.isalpha() or dd.isalpha():
                raise ValueError

            # Validate date and print new format
            if 0 < int(dd) < 32 and 0 < int(mm) < 13 and int(yyyy) >= 0:
                print(f"{yyyy}-{mm.zfill(2)}-{dd.zfill(2)}")
            else:
                raise ValueError

            # End program
            break

        # Handle ValueError exception that may occur
        except ValueError:
            pass


main()