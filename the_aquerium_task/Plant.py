from Creature import Creature


class Plant(Creature):
    def needs_food(self):
        return self.food_level < 15

    def eat(self, food):
        self.food_level += food * 0.5
