import random
import string

# Dummy database of users and passwords
user_db = {
    admin: password123
}

def generate_reset_code():
    Generates a temporary reset code.
    code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return code

def forgot_password(username):
    Handles the forgot password process.
    # Check if user exists
    if username in user_db:
        reset_code = generate_reset_code()
        print(fYour reset code is: {reset_code})  # In real use, this would be sent to the user's email.
        
        # Ask user to enter the reset code
        entered_code = input(Enter the reset code you received: )
        
        # Validate the reset code
        if entered_code == reset_code:
            new_password = input(Enter a new password: )
            user_db[username] = new_password
            print(Your password has been successfully reset!)
        else:
            print(Invalid reset code.)
    else:
        print(Username not found.)

# Example usage
username = input(Enter your username: )
forgot_password(username)

