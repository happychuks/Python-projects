from shirt import Shirt

happy_Shirt = Shirt('red', 'L', 'short sleeve', 12000)

print(happy_Shirt.get_price())
#or
print(happy_Shirt.price)

happy_Shirt.set_price(14000)

print(happy_Shirt.price)

print(happy_Shirt.discount_price(.5))

shirt_one = Shirt('red', 'S', 'short', 12)
shirt_two = Shirt('orange', 'L', 'short-sleeve', 10)

total = shirt_one.price + shirt_two.price

total_discount =  shirt_one.discount(.14) + shirt_two.discount(.06) 

tshirt_collection = []
shirt_one = Shirt('orange', 'M', 'short sleeve', 25)
shirt_two = Shirt('red', 'S', 'short sleeve', 15)
shirt_three = Shirt('purple', 'XL', 'short sleeve', 10)


tshirt_collection.append(shirt_one)
tshirt_collection.append(shirt_two)
tshirt_collection.append(shirt_three )

for i in range(tshirt_collection):
   print (tshirt_collection[i].color)