import unittest
from Temperature_Converter import celsius_to_fahrenheit, fahrenheit_to_celsius


class TestTemperatureConverter(unittest.TestCase):
    def test_freezing_point(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)

    def test_boiling_point(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_minus_40(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40)
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40)

    def test_convert_celsius_and_back(self):
        original_celsius = 25
        fahrenheit = celsius_to_fahrenheit(original_celsius)
        converted_back = fahrenheit_to_celsius(fahrenheit)

        self.assertAlmostEqual(converted_back, original_celsius)

    def test_convert_fahrenheit_and_back(self):
        original_fahrenheit = 77
        celsius = fahrenheit_to_celsius(original_fahrenheit)
        converted_back = celsius_to_fahrenheit(celsius)

        self.assertAlmostEqual(converted_back, original_fahrenheit)


if __name__ == "__main__":
    unittest.main()