# Password Generator
import string
import random

print("Welcome to the PyPassword Generator!")

letters = int(input("How many letters would you like in your password? "))
symbols = int(input("How many symbols would you like in your password? "))
numbers = int(input("How many numbers would you like in your password? "))

letter_list = list(string.ascii_letters)
symbol_list = list('!#$%&()*+')
number_list = list(string.digits)

subset_letter = random.choices(letter_list, k=letters)
subset_symbol = random.choices(symbol_list, k=symbols)
subset_number = random.choices(number_list, k=numbers)

password_list = subset_letter + subset_symbol + subset_number
random.shuffle(password_list)

password = ''.join(password_list)

print("Your generated password is:", password)