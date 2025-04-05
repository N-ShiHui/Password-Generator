import random

print("Looking to find a strong password? We can help with that!")
nr_uppercase = int(input(f"How many uppercase letters would you like in your password?\n"))
nr_lowercase = int(input(f"How many lowercase letters would you like?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

uppercase = []
for i in range(65, 91):
    uppercase.append(chr(i))

lowercase = []
for i in range(97, 123):
    lowercase.append(chr(i))

symbols = []
for i in range(33, 48):
    symbols.append(chr(i))

numbers = []
for num in range(0, 10):
    numbers.append(str(num))

password_list = []
for char in range(1, nr_uppercase + 1):
    password_list.append(random.choice(uppercase))

for char in range(1, nr_lowercase + 1):
    password_list.append(random.choice(lowercase))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
password = ""
for i in password_list:
    password += i

print(f"Your password is: {password}")


