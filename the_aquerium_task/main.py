from Aquarium import Aquarium
from Fish import Fish
from Plant import Plant


def main():
    aquarium = Aquarium()

    aquarium.add_creature(Fish("goldfish"))
    aquarium.add_creature(Fish("clownfish"))
    aquarium.add_creature(Plant("seaweed"))
    aquarium.add_creature(Plant("kelp"))

    print("Before feeding:")
    aquarium.display_status()

    print("After feeding with 50:")
    print("Feeding with 50")
    aquarium.feed(50)
    aquarium.display_status()

    print("After feeding with 80:")
    print("Feeding with 80")
    aquarium.feed(80)
    aquarium.display_status()


if __name__ == "__main__":
    main()
