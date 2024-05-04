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

def save_to_file(passwords):
    filename = input("Enter filename to save passwords (e.g., passwords.txt): ")
    try:
        with open(filename, 'w') as file:
            for password in passwords:
                file.write(password + '\n')
        print("Passwords saved to", filename)
    except Exception as e:
        print("Error:", e)

def improve_password(password):
    improved_password = ''
    for char in password:
        if char == 'a':
            improved_password += '@'
        elif char == 'o':
            improved_password += '0'
        elif char == 'l':
            improved_password += '1'
        elif char == 's':
            improved_password += '$'
        elif char == 'e':
            improved_password += '3'
        elif char == 'i':
            improved_password += '1'
        else:
            improved_password += char
    return improved_password

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

        save_option = input("Do you want to save these passwords to a file? (y/n): ").lower()
        if save_option == 'y':
            save_to_file(passwords)

        improve_option = input("Do you want to improve any of these passwords? (y/n): ").lower()
        if improve_option == 'y':
            improved_passwords = []
            for password in passwords:
                improve = input("Improve password '{}'? (y/n): ".format(password)).lower()
                if improve == 'y':
                    improved_passwords.append(improve_password(password))
                else:
                    improved_passwords.append(password)
            print("\nImproved Passwords:")
            for password in improved_passwords:
                print(password)
    except ValueError:
        print("Error: Please enter valid integer values for number of passwords and password length.")

if __name__ == "__main__":
    main()
