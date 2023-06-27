import sys
import re
import inflect
import datetime


def main():
    print(calculate_minutes(get_dob("Date of Birth: ")))


def get_dob(prompt):
    try:
        dob = input(prompt)

        # Check correct format of DOB
        if match:= re.search("^(\d{4})-(\d\d)-(\d\d)$", dob):

            # Check there's no more than 12 months
            if match.group(2) > "12":

                # Check correct number of days, depending the input month
                if match.group(2) in [1, 3, 5, 7, 8, 10, 12] and match.group(3) > "31":
                    sys.exit("Invalid date")
                elif match.group(2) in [4, 6, 9, 11] and match.group(3) > "30":
                    sys.exit("Invalid date")
                elif match.group(3) > "29":
                    sys.exit("Invalid date")
        else:
            sys.exit("Invalid date")

        # If OK, return DOB
        return dob
    except:
        sys.exit("Invalid date")


def calculate_minutes(dob):
    # Define today
    year, month, day = str(datetime.date.today()).split("-")
    today = datetime.datetime(int(year), int(month), int(day), 0, 0, 0)

    # Define date of birth
    dob_year, dob_month, dob_day = str(dob).split("-")
    dob = datetime.datetime(int(dob_year), int(dob_month), int(dob_day), 0, 0, 0)

    # Get difference
    delta = today - dob

    # Print minutes in words
    p = inflect.engine()
    return f"{p.number_to_words(int(delta.total_seconds()/60)).capitalize().replace('and ', '')} minutes"


if __name__ == "__main__":
    main()