# Dummy login script

# Predefined username and password (for demo purposes)
USERNAME = admin
PASSWORD = password123

def login():
    # Get input from the user
    entered_username = input(Enter username: )
    entered_password = input(Enter password: )

    # Check credentials
    if entered_username == USERNAME and entered_password == PASSWORD:
        print(Login successful!)
    else:
        print(Invalid username or password. Please try again.)

# Run the login function
login()

