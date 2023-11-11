class Shirt:
    def __init__(self, shirt_color, shirt_size, shirt_type, shirt_price):
        self.color = shirt_color
        self.size = shirt_price
        self.type = shirt_type
        self.price = shirt_price
    
    def get_price(self):
        return self.price
    
    def set_price(self, shirt_price):
        self.price = shirt_price

    def discount_price(self, discount):
        return self.price * (1 - discount) 

happy_Shirt = Shirt('red', 'L', 'short sleeve', 12000)

print(happy_Shirt.get_price())
#or
print(happy_Shirt.price)

happy_Shirt.set_price(14000)

print(happy_Shirt.price)

print(happy_Shirt.discount_price(.5))
