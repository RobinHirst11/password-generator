import random
import string

def generate_password(length=12, use_symbols=True, use_numbers=True):
    characters = string.ascii_letters
    if use_symbols:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    length = int(input("Enter desired password length: "))
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    
    password = generate_password(length, use_symbols, use_numbers)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
