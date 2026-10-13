class Aquarium:
    def __init__(self):
        self.creatures = []

    def add_creature(self, creature):
        self.creatures.append(creature)

    def feed(self, food):
        hungry_creatures = []

        for creature in self.creatures:
            if creature.needs_food():
                hungry_creatures.append(creature)

        if len(hungry_creatures) > 0:
            food_per_creature = food / len(hungry_creatures)

            for creature in hungry_creatures:
                creature.eat(food_per_creature)

    def display_status(self):
        for creature in self.creatures:
            if creature.needs_food():
                print(f"The {creature.name} needs food")
            else:
                print(f"The {creature.name} doesn't need food")
