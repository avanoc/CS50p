from validator_collection import checkers

# Check if the user's input has email syntax
if checkers.is_email(input("What's your email? ")):
    print("Valid")
else:
    print("Invalid")