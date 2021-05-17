from order import Order

class Customer:

    """Class of Customer which will have an id number, name, and a list of all the customers orders"""
    
    def __init__(self):
        self.id = ""
        self.name = ""
        self.orders = [] #creates a list of orders for the customer

    def get_order_count(self):
        """Returns the length of the order list to show how many orders there are"""
        return len(self.orders)

    def get_total(self):
        total = 0
        for x in self.orders:
            total += x.get_total()
        return total

    def add_order(self, order):
        self.orders.append(order)

    def display_summary(self):
        print("Summary for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))
        print("Orders: {}".format(self.get_order_count()))
        print("Total: ${:.2f}".format(self.get_total()))


    def display_receipts(self):
        print("Detailed receipts for customer '{}':".format(self.id))
        print("Name: {}".format(self.name))

        for x in self.orders:
            print()
            x.display_receipt()
            
