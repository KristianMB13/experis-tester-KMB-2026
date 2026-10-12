def quarter_of_the_year(month):
    if month <= 3:
        return "1st quarter"
    elif month <= 6:
        return "2nd quarter"
    elif month <= 9:
        return "3rd quarter"
    else:
        return "4th quarter"


print(quarter_of_the_year(3))
print(quarter_of_the_year(10))