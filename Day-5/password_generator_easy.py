import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword:")
print("How many letters would you like in your password?")
no_letters=int(input())
print("How many symbols would you like?")
no_symbols=int(input())
print("How many numbers would you like?")
no_numbers=int(input())

password=""
for i in range(1,no_letters+1):
    password=password+random.choice(letters)
for i in range(1,no_symbols+1):
    password=password+random.choice(symbols)
for i in range(1,no_numbers+1):
    password=password+random.choice(numbers)
    

print(f"here is your Password: {password}")
 