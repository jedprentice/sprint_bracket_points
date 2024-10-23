from points_calculator import DriverPoints


def check_calculations(data: list[str], points: list[int], driver: str, total: int,
                       total_with_drops: int) -> None:
    driver_points = DriverPoints(data)
    assert driver == driver_points.driver
    assert points == driver_points.points
    assert total == driver_points.total()
    assert total_with_drops == driver_points.total_with_drops()


def test_calculate() -> None:
    data = ["Jed Prentice", "", "1780", "100", "80", "80", "0", "0", "", "100", "75", "80", "75",
            "100", "100", "0", "0", "", "80", "100", "100", "100", "65", "50", "80", "65", "100",
            "100", "75", "75"]
    points = [100, 80, 80, 0, 0, 100, 75, 80, 75, 100, 100, 0, 0, 80, 100, 100, 100, 65, 50, 80,
              65, 100, 100, 75, 75]
    check_calculations(data, points, "Jed Prentice", 1780, 1525)


def test_calculate_another() -> None:
    data = ["Christopher Graham", "", "1315", "80", "100", "100", "0", "0", "", "0", "0", "0",
            "80", "100", "100", "0", "0", "", "100", "100", "80", "100", "100", "100", "100", "75",
            "0", "0", "0", "0"]
    points = [80, 100, 100, 0, 0, 0, 0, 0, 80, 100, 100, 0, 0, 100, 100, 80, 100, 100, 100, 100,
              75, 0, 0, 0, 0]
    check_calculations(data, points, "Christopher Graham", 1315, 1315)
