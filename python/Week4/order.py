
from product import Product

class Order:

    """Class of Order which will have an id number and will take products and add it to a list"""

    def __init__(self):
        self.id = ""
        self.products = []
    
    def get_subtotal(self):
        s_total = 0
        for x in self.products: #iterate through the list of products to get the total price of each product
            s_total += x.get_total_price() #adds the total price of each product to the subtotal
        return s_total

    def get_tax(self):
        return self.get_subtotal() * .065

    def get_total(self):
        return self.get_tax() + self.get_subtotal()

    def add_product(self, product):
        """Adds a products with 4 variables to the list of products"""
        self.products.append(product)

    def display_receipt(self):
        print("Order: {}".format(self.id))
        for p in self.products: #iterate through the products list and display each product
            p.display()
        print("Subtotal: ${:.2f}".format(self.get_subtotal()))
        print("Tax: ${:.2f}".format(self.get_tax()))
        print("Total: ${:.2f}".format(self.get_total()))