import random
import string

print("Welcome to the SecurePass Generator!\n")

length = int(input("How long should your password be? "))
include_upper = input("Include uppercase letters? (y/n) ").lower() == "y"
include_numbers = input("Include numbers? (y/n) ").lower() == "y"
include_symbols = input("Include symbols? (y/n) ").lower() == "y"

if length <= 0:
    print("Error: Password length must be greater than 0!")
    exit()

characters = list(string.ascii_lowercase)

if include_upper:
    characters += list(string.ascii_uppercase)
if include_numbers:
    characters += list(string.digits)
if include_symbols:
    characters += list("!@#$%^&*()-_=+[]{};:,.<>?/")

if len(characters) < 1:
    print("You must select at least one character type!")
else:
    password = "".join(random.choice(characters) for character in range(length))
    print("\nYour secure password is: " + password)

types_used = sum([include_upper, include_numbers, include_symbols])
if types_used == 0:
    strength = "Easy"
elif types_used == 1:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength:", strength)

shuffle = input("\nGenerate a second shuffled version? (y/n): ").lower()
if shuffle == "y":
    password_list = list(password)
    random.shuffle(password_list)
    print("Shuffled version: " + "".join(password_list))
