print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
fullnames = name1 + name2
lower_fullnames = fullnames.lower()
t = lower_fullnames.count("t")
r = lower_fullnames.count("r")
u = lower_fullnames.count("u")
e = lower_fullnames.count("e")
first_digit = t + r + u + e
l = lower_fullnames.count("l")
o = lower_fullnames.count("o")
v = lower_fullnames.count("v")
e = lower_fullnames.count("e")
second_digit = l + o + v + e
score = int(str(first_digit) + str(second_digit))
if (score < 10) or (score > 90):
  print(f"Your score is {score}, you go together like coke and mentos.")
elif(score >= 40) and (score <= 50):
  print(f"Your score is {score}, you are alright together.")
else:
  print(f"Your score is {score}.")
