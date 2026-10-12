from BaseProduct import BaseProduct

class Product(BaseProduct):
    name = ""
    price = 0.0
    quantity = 0
    location = ""
    weight = 0


    def __init__(self, name, price, quantity, location, weight):
        super().__init__(name, price)
        self.quantity = quantity
        self.location = location
        self.weight = weight

    def is_in_stock(self):
        return self.quantity > 0

    def get_total_value(self):
        return self.price * self.quantity

    def restock(self, additional_quantity):
        self.quantity += additional_quantity

    @staticmethod
    def is_valid_product_name(name):
        return isinstance(name, str) and len(name) > 0

    def __str__(self):
        return(f"Product Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}, Location: {self.location}, Weight: {self.weight}")