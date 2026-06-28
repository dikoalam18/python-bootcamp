# Ask the user for an input
email_input = input("\nEnter your email address: ")

# TODO: If valid gmail address
is_valid = email_input.endswith("@gmail.com")
if is_valid:
    print("\nThis is a valid gmail address")
else:
    print("\nThis is NOT a valid gmail address")
