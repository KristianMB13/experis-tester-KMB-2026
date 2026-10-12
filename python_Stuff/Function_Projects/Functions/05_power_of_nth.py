def index(numbers, n):
    if n >= len(numbers):
        return 1

    return numbers[n] ** n


print(index([1, 2, 3, 4], 2))
print(index([1, 2, 3, 4], 5))