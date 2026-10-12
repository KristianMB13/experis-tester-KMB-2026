def food_menu(foods):
    menu = []

    for position, food in enumerate(foods, start=1):
        menu.append(f"{position}. {food}")

    return menu


print(food_menu(["Hawaii Pizza", "Diablo Pizza"]))