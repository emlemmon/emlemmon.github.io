
class Product:

    """Class of Product with an id number, a name, a price and a quantity as well as two methods"""

    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def get_total_price(self):
        return self.price * self.quantity
    
    def display(self):
        """Displays the product name, the quantity, and the total price of them"""
        print("{} ({}) - ${:.2f}".format(self.name, int(self.quantity), float(self.get_total_price())))



