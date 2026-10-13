import unittest
from Fish import Fish
from Plant import Plant


class TestAquarium(unittest.TestCase):

    def test_goldfish(self):
        goldfish = Fish("Goldfish", 0)
        goldfish.update_food_level(20)
        self.assertEqual(goldfish.food_level, 12)

    def test_seaweed(self):
        seaweed = Plant("Seaweed", 0)
        seaweed.update_food_level(20)
        self.assertEqual(seaweed.food_level, 10)


if __name__ == "__main__":
    unittest.main()