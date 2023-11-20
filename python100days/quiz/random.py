import random

names_string = input("Enter list of names seperated by comma")
names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.


random_name = random.randint(0, len(names)-1) #this generates random number btw 0 and length of the list

print(f"{names[random_name]} is going to buy the meal today!")