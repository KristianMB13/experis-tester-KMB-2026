def remove_orders(orders):
    order_list = orders.split(",")
    remaining_orders = order_list[1:-1]
    return ",".join(remaining_orders)


print(remove_orders("1,2,3,4"))