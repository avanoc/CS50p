def main():
    # Prompt user for time:
    time = input("What time is it? ")

    # Format time:
    time = convert(time)

    # Return meal:
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")

def convert(time):
    if "p.m." in time:
        hour = int(time.split(":")[0]) + 12
    else:
        hour = int(time.split(":")[0])
    minutes = float(time.split(":")[1])/60
    time = hour + minutes
    return(time)


if __name__ == "__main__":
    main()