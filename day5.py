import random

print("Welcome to SnowPassword Generator!")

len_letters = int(input("How many letters would you like in your password? \n"))
len_symbols = int(input("How many symbols would you like? \n"))
len_numbers = int(input("How many numbers would you like? \n"))

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ['!', '@', '}', ')', '(', '&', '^', '-', '_', '$', '%', '#']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

password_list = []

for i in range(len_letters):
    password_list.append(random.choice(letters))

for i in range(len_symbols):
    password_list.append(random.choice(symbols))

for i in range(len_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''.join(password_list)
print("Your generated password is:", password)






