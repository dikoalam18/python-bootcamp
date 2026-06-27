# Expected username and password (you can change the value)
correct_username = "user"
correct_password = "pass"
admin_username = "admin"
admin_password = "admin"

# Enter username and password
username_input = input("Please provide username: ")
password_input = input("Please provide password: ")

# TODO: Notify user if credentials are valid or invalid
is_correct_username = correct_username == username_input
is_correct_password = correct_password == password_input
user_correct_credentials = is_correct_username and is_correct_password

is_admin_username = admin_username == username_input
is_admin_password = admin_password == password_input
admin_correct_credentials = is_admin_username and is_admin_password

correct_credentials = admin_correct_credentials or user_correct_credentials

if correct_credentials:
    print("Access Granted")
else:
    print("Access Denied")
