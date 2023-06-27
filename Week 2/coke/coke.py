# Set base values
due = 50
paid = 0

# Ask for payment until the coke is fully paid
while due >= 0:
    print("Amount due: " + str(due))
    if due == 0:
        break
    else:
        paid = int(input("Insert coin: "))
        if paid == 25 or paid == 10 or paid == 5:
            due = due - paid

# if there's change left, inform the user
if due < 0:
    print("Change owed: " + str(abs(due)))