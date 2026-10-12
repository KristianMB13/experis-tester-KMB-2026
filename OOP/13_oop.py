from Product import Product


# class Product:
#     name = ""
#     price = 0.0
#     quantity = 0
#     location = ""

#     def __init__(self, name, price, quantity, location, weight):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.location = location
#         self.weight = weight

#     def is_in_stock(self):
#         return self.quantity > 0

#     def apply_discount(self, discount_percentage):
#         discount_value = self.price * (discount_percentage / 100)
#         self.price -= discount_value

#     def restock(self, additional_quantity):
#         self.quantity += additional_quantity




#white_tea = Product()
#white_tea.name = "White Tea"
#white_tea.price = 120
#white_tea.quantity = 40
#white_tea.location = "Store A"
#white_tea.weight = 10


white_tea = Product("White Tea", 120, 40, "Store A", 10)


# print(white_tea.name)
# print(white_tea.is_in_stock())

white_tea.price = 100

white_tea.apply_discount(10)
print(white_tea.price)

white_tea.restock(20)
print(white_tea.quantity)

