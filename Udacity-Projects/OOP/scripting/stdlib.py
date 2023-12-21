import math
import random

# list all the library names in the requirements.txt with their version
"""Example: requirements.txt
beautifulsoup4==4.5.1
bs4==0.0.1
pytz==2016.7
requests==2.11.1
"""
# pip install -r requirements.txt (To install all libraries in the requirements.txt file)
result = math.exp(3)
print(result)

# We begin with an empty `word_list`
word_file = "camelot.txt"
word_list = []

# We fill up the word_list from the `words.txt` file
with open(word_file,'r') as words:
    for line in words:
        # remove white space and make everything lowercase
        word = line.strip().lower()
        # don't include words that are too long or too short
        if 3 < len(word) < 8:
            word_list.append(word)

# TODO: Add your function generate_password below
def generate_password():
    return random.choice(word_list) + str(random.randint(0, 9)) + random.choice(word_list) + random.choice(word_list)
# It should return a string consisting of three random words 
# concatenated together without spaces

# Now we test the function
password = generate_password()
print(password)