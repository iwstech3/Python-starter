import random
import string

# Get user input for the number of digits, letters, and symbols in the password
num_digits = int(input("Enter the number of digits in the password: "))
num_letters = int(input("Enter the number of letters in the password: "))
num_symbols = int(input("Enter the number of symbols in the password: "))

# Define character sets for digits, letters, and symbols
digits = string.digits
letters = string.ascii_letters
symbols = string.punctuation

# Generate random digits
password_digits = ''.join(random.choices(digits, k=num_digits))
print(digits)
print(letters)
print(symbols)

# Generate random letters


# Generate random symbols


# Combine all characters and shuffle them to create the password
# password_list = list(password_digits + password_letters + password_symbols)
# random.shuffle(password_list)
# password = ''.join(password_list)

# Print the generated password
# print("Generated Password:", password)