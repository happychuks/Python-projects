import random
#pool of characters to generate password from
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Python Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = []

for i in range(1, nr_letters + 1):
  password.append(random.choice(letters))

for i in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))

for i in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))

random.shuffle(password)
print(password) #output is in characters separate by comma

#to join them as a string
passwordGenerated = ""
for char in password:
  passwordGenerated += char
print(f"Your newly generated password is: {passwordGenerated}")

#OR simply just use the .join function
print("Your password is: " + "".join(password))