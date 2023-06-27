# Prompt user for expression:
expression = input("Expression: ").split(" ", 2)

# Retrieve ints and operators:
x = int(expression[0])
operator = expression[1]
z = int(expression[2])

# Do the math:
if operator == "+":
    print(float(x + z))
elif operator == "-":
    print(float(x - z))
elif operator == "*":
    print(float(x * z))
elif operator == "/":
    print (float(x / z))