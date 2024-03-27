import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True):
    characters = string.ascii_letters
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords, length=12, use_symbols=True, use_numbers=True):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(length, use_symbols, use_numbers)
        passwords.append(password)
    return passwords

def main():
    try:
        num_passwords = int(input("Enter the number of passwords to generate: "))
        length = int(input("Enter desired password length: "))
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
        
        passwords = generate_multiple_passwords(num_passwords, length, use_symbols, use_numbers)
        
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)
    except ValueError:
        print("Error: Please enter valid integer values for number of passwords and password length.")

if __name__ == "__main__":
    main()
