def main():
    count()


def count():

    # Set empty list
    grocery = []

    while True:
        # Add items to the list
        try:
            item = input().upper()
            grocery.append(item)

        # Print out list when ctrl-d is hit
        except EOFError:
            print()
            grocery.sort()

            # Create a clean list without replicates
            clean = list(dict.fromkeys(grocery))
            for item in clean:

                # Don't print more than once
                if grocery.count(item) > 1:
                    print(f"{grocery.count(item)} {item}")

                # print how many items there are and the items name
                else:
                    print(f"{grocery.count(item)} {item}")
            break


main()