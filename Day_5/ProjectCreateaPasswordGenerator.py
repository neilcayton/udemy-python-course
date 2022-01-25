# 8. Day 5 Project Create a Password Generator

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password? "
                       "\n"))
nr_symbols = int(input("How many symbols would you like? "
                       "\n"))
nr_numbers = int(input("How many number would you like? "
                       "\n"))

# easy level
password = []
for characters in range(1, nr_letters+1):
    length = len(letters) - 1
    randomizer = random.randint(0, length)
    output = str(letters[randomizer])
    password += str(output)
print(password)

for characters in range(1, nr_symbols+1):
    length = len(symbols) - 1
    randomizer = random.randint(0, length)
    output = str(symbols[randomizer])
    password += str(output)
print(password)

for characters in range(1, nr_numbers+1):
    length = len(numbers) - 1
    randomizer = random.randint(0, length)
    output = str(numbers[randomizer])
    password += str(output)
print(password)
password_list = ''.join([str(item) for item in password])
print(f"here is the password \n"
      f"{password_list}")

# harder level

randomized_pass = password
random.shuffle(randomized_pass)
string = ''.join([str(item) for item in randomized_pass])
print(f"here is your mixed password:\n"
      f"{string}")