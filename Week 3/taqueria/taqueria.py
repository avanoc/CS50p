def main():
    order("Item: ")


def order(prompt):
    # Create a dictionary with the menu
    menu = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
    }

    # Set base price to zero
    price = 0

    while True:

        # Prompt user for food, check if it's on the menu and print the sum of the amount due
        try:
            item = input(prompt).title()
            for food in menu:
                if item == food:
                    price = price + menu[item]
                    print("Total: $%.2f" % price)

        # break out of loop when "ctrl + d"
        except EOFError:
            break


main()