from unittest import TestCase
from points_calculator import PointsCalculator


class PointsCalculatorTest(TestCase):
    def test_calculate(self) -> None:
        data = "Jed Prentice,,1430,100,80,80,,,,100,75,80,75,100,100,,,,80,100,100,100,65,50,80,65,,,,,,,\n".split(",")
        points = [100, 80, 80, 0, 0, 100, 75, 80, 75, 100, 100, 0, 0, 80, 100, 100, 100, 65, 50, 80, 65]
        calculator = PointsCalculator(data)
        self.assertEqual("Jed Prentice", calculator.driver, "Wrong driver")
        self.assertEqual(points, calculator.points)
        self.assertEqual(1430, calculator.total(), "Incorrect total")
        self.assertEqual(1380, calculator.total_with_drops(), "Incorrect total with drops")

    def test_calculate_another(self) -> None:
        data = "Christopher Graham,,1315,80,100,100,,,,,,,80,100,100,,,,100,100,80,100,100,100,100,75,,,,,,,\n".split(",")
        points = [80, 100, 100, 0, 0, 0, 0, 0, 80, 100, 100, 0, 0, 100, 100, 80, 100, 100, 100, 100, 75]
        calculator = PointsCalculator(data)
        self.assertEqual("Christopher Graham", calculator.driver, "Wrong driver")
        self.assertEqual(points, calculator.points)
        self.assertEqual(1315, calculator.total(), "Incorrect total")
        self.assertEqual(1315, calculator.total_with_drops(), "Incorrect total with drops")
