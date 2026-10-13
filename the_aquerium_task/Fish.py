from Creature import Creature


class Fish(Creature):
    def needs_food(self):
        return self.food_level < 10

    def eat(self, food):
        self.food_level += food * 0.6
