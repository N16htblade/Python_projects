import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

temppass = []

for char in range (1, nr_letters + 1):
    temppass.append(letters[random.randint(0, len(letters)-1)])

for char in range (1, nr_symbols + 1):
    temppass.append(symbols[random.randint(0, len(symbols)-1)])

for char in range (1, nr_numbers + 1):
    temppass.append(numbers[random.randint(0, len(numbers)-1)])

random.shuffle(temppass)
password = ''.join(temppass)

# while len(temppass) > 0:
#     randIndex = random.randint(0,len(temppass) - 1)
#     password = password + temppass[randIndex]
#     temppass.pop(randIndex)

print (f"Your new Password should be:\n{password}")