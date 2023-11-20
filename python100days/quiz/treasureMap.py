line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
if position == "A1" or position == "A2" or position == "A3":
  if position == "A1":
    line1[0] = "X"
  if position == "A2":
    line2[0] = "X"
  if position == "A3":
    line3[0] = "X"
if position == "B1" or position == "B2" or position == "B3":
  if position == "B1":
    line1[1] = "X"
  if position == "B2":
    line2[1] = "X"
  if position == "B3":
    line3[1] = "X"
if position == "C1" or position == "C2" or position == "C3":
  if position == "C1":
    line1[2] = "X"
  if position == "C2":
    line2[2] = "X"
  if position == "C3":
    line3[2] = "X"
# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")

#second method
letter = position[0].lower()  #stores the first character which is a letter
abc = ["a", "b", "c"]
letter_index = abc.index(letter) #checks for the index of the letter
number_index = int(position[1]) - 1 #stores the 2nd character which is an int
map[number_index][letter_index] = "X" #e.g B3, the map is first located with the number index and then the letter index
print(f"{line1}\n{line2}\n{line3}")
