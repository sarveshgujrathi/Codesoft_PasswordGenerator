import random
import string

def generate_password(length):
    # Define character sets to choose from
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password with the specified length
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt the user for password length
    try:
        length = int(input("Enter the desired password length: "))
        if length <= 0:
            print("Please enter a positive integer for the length.")
            return
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return
    
    # Generate the password
    password = generate_password(length)
    
    # Display the generated password
    print(f"Generated Password: {password}")

# Run the password generator
if _name_ == "_main_":
    main()