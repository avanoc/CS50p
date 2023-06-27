# Prompt user for the Answer:
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

# Check if the Answer is correct:
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")