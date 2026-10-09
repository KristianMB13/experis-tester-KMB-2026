def calculate_total_and_discount(order_amount, shipping_fee):
    discount = 0.15 if order_amount > 200 else 0.05
    total = (order_amount - (order_amount * discount)) + shipping_fee
    return total, discount

my_total, my_discount = calculate_total_and_discount(2000, 100)

print(f"My Total = ${my_total}")

print(f"My Discount = ${my_discount}")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

print(f"Red: {red}")