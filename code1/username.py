# Simple script to create a username

def create_username(first_name, last_name):
    # Convert names to lowercase and concatenate
    username = (first_name[:3] + last_name[:3]).lower()
    return username

# Get input from the user
first_name = input(Enter your first name: )
last_name = input(Enter your last name: )

# Generate and display username
username = create_username(first_name, last_name)
print(fYour new username is: {username})

