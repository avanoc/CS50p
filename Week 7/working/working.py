import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    # assign "s" to the match from the string the user has input, using the RE for the expected format
    try:
        if re.search(r"(.?.?:?.?.?) (AM|PM) to (.?.?:?.?.?) (AM|PM)", s, re.IGNORECASE):
            s = re.search(r"(.?.?:?.?.?) (AM|PM) to (.?.?:?.?.?) (AM|PM)", s, re.IGNORECASE)

        # If the format is not as expected, raise a ValueError
        else:
            raise ValueError

    except ValueError:
        sys.exit("ValueError")

    # Catch the time of start and finish from the RE syntax
    start = s.group(1)
    finish = s.group(3)

    try:
        # Style the time format whether there's a ":" in the input or not, both in starting and finishing times
        if ":" in start:
            s_hours, s_minutes = start.split(":")
        else:
            s_hours = start
            s_minutes = "00"

        if ":" in finish:
            f_hours, f_minutes = finish.split(":")
        else:
            f_hours = finish
            f_minutes = "00"

        # Check that the minutes retrieved are valid
        if (s_minutes or f_minutes) >= "60":
            raise ValueError

    except ValueError:
        sys.exit("ValueError")

    # Add extra zero to the hour if necessary
    s_hours = s_hours.zfill(2)
    f_hours = f_hours.zfill(2)

    # If starting time is in the morning, print hours in morning format. 12 AM prints as 00
    if s.group(2) == "AM":
        if s_hours == "12":
            s_hours = "00"
        start = f"{s_hours}:{s_minutes}"
    # If starting time is after noon, add 12 hours, unless it's 12 PM
    else:
        if s_hours != "12":
            s_hours = int(s_hours) + 12
        start = f"{s_hours}:{s_minutes}"

    # If finishing time is in the morning, print hours in morning format. 12 AM prints as 00
    if s.group(4) == "AM":
        if f_hours == "12":
            f_hours = "00"
        finish = f"{f_hours}:{f_minutes}"

    # If finishing time is after noon, add 12 hours, unless it's 12 PM
    else:
        if f_hours != "12":
            f_hours = int(f_hours) + 12
        finish = f"{f_hours}:{f_minutes}"

    # Return the formatted time
    return f"{start} to {finish}"

if __name__ == "__main__":
    main()