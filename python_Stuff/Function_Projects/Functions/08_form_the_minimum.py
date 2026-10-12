def form_the_minimum(digits):
    smallest_digits = sorted(set(digits))
    number = ""

    for digit in smallest_digits:
        number += str(digit)

    return int(number)


print(form_the_minimum([1, 3, 6, 2, 3]))