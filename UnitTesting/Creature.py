class Creature:
    def __init__(self, name, food_level, needs_food_below, absorption):
        self.name = name
        self.food_level = food_level
        self.needs_food_below = needs_food_below
        self.absorption = absorption

    def needs_food(self):
        return self.food_level < self.needs_food_below

    def update_food_level(self, food):
        if self.needs_food():
            self.food_level += food * self.absorption / 100

    def __str__(self):
        return f"Name: {self.name}, Food level: {self.food_level}, needs food below: {self.needs_food_below}"
