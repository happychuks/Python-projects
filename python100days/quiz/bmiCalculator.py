# 1st input: enter height in meters e.g: 1.65
height = input()
# 2nd input: enter weight in kilograms e.g: 72
weight = input()
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height_float = float(height)
weight_int = int(weight)
bmi = int(weight_int / height_float ** 2)
print(bmi)