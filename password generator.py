import random
import string

def generate_password(length, use_letters=True, use_numbers=True, use_special=True):
    characters = ''
    if use_letters:
        characters += string.ascii_letters
    if use_numbers:
        characters += string.digits
    if use_special:
        # here i am adding some special characters..
        special_characters = '@#$&*_~'
        characters += special_characters

    # Generate password
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def get_length():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please! enter a positive integer greater than 0.")
            else:
                return length
        except ValueError:
            print("Please enter a valid integer.")

def yes_no(prompt):
    while True:
        response = input(prompt).lower()
        if response in ['yes', 'no', 'y', 'n']:
            return response in ['yes', 'y']
        else:
            print("Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the password generator.....")
    # Get user input for password length
    length = get_length()
    # take input from user
    use_letters = yes_no("Include letters (yes/no)? ")
    use_numbers = yes_no("Include numbers (yes/no)? ")
    use_special = yes_no("Include special characters (yes/no)? ")

    # Generate and print password
    password = generate_password(length, use_letters, use_numbers, use_special)
    print("Here Your generated password is:", password)
main()
