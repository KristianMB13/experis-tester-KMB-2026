def basic_operations(operation, number1, number2):
    if operation == "add":
        return number1 + number2
    elif operation == "subtract":
        return number1 - number2
    elif operation == "multiply":
        return number1 * number2
    elif operation == "divide":
        return number1 / number2


print(basic_operations("add", 10, 5))
print(basic_operations("subtract", 10, 5))
print(basic_operations("multiply", 10, 5))
print(basic_operations("divide", 10, 5))