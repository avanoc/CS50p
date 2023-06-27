constant = 300000000

# Get mass in Kg from user:
mass = int(input("Please enter a mass, in Kg: "))

energy = mass * (constant**2)
print("E: ", energy)