# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
is_correct_username = correct_username == username_input
is_correct_password = correct_password == password_input
correct_credentials = is_correct_username and is_correct_password

if correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")
