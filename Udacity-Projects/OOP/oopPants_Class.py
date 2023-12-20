class Pants:
    """The Pants class represents an article of clothing sold in a store
    """
    def __init__(self, pant_color, waist_size, pant_type, pant_price):
        """Method for initializing a Pants object
    
        Args: 
            pant_color (str)
            waist_size (int)
            pant_type (str)
            pant_price (float)
            
        Attributes:
            pant_color (str): color of a pants object
            waist_size (str): waist size of a pants object
            pant_type (str): type of a pant object
            pant_price (float): price of a pants object
        """
        self.color = pant_color
        self.size = waist_size
        self.type = pant_type
        self.price = pant_price
    
    def get_price(self):
        return self.price
    
    def set_price(self, pant_price):
        self.price = pant_price
    
felixPant = Pants('black', 'm', 'cotton', 3500)

print(felixPant.get_price())
felixPant.set_price(4000)
print(felixPant.get_price())