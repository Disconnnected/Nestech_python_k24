"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password
"""

"""
upper case = "sfdasffsadf"
upper case = "sfdasffsadf"
upper case = "sfdasffsadf"
upper case = "sfdasffsadf"
"""


import random, string

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digit = string.digits
symbol = string.punctuation
letter = uppercase + lowercase + digit + symbol

def generate_password(len):
    password = ""
    for i in range(1,len+1):
        password = password + random.choice(letter)
    print(password)
    if check_password(password):
        print(f"Valid password is: {password}")
        return True

def check_password(password):
    is_uppercase = False
    is_lowercase = False
    is_digit = False
    is_symbol = False

    for char in password:
        # _P/GN}a]
        if char in uppercase:
            is_uppercase = True
        elif char in lowercase:
            is_lowercase = True        
        elif char in digit:
            is_digit = True
        elif char in symbol:
            is_symbol = True
    if is_uppercase == True \
        and is_lowercase == True \
        and is_digit == True \
        and is_symbol == True:
        return True
    else:
        return False

while True:
    print("generating...")
    if generate_password(8):
        break

# print(password)

# generate_password(8)
