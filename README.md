# Predefined username and password
USERNAME = "admin"
PASSWORD = "12345"

# Ask user for input
username_input = input("Enter username: ")
password_input = input("Enter password: ")

# Check login
if username_input == USERNAME and password_input == PASSWORD:
    print("Login successful!")
else:
    print("Invalid username or password.")
