import csv

DROPS = 6
RACES = 24
ROWS_TO_SKIP = 2


def parse_value(s: str) -> int:
    if s == "":
        return 0
    return int(s)


class DriverPoints:
    def __init__(self, data: list[str]):
        self.driver = data[0]
        self.points = []
        # Trailing comma adds a zero at the end, skip it
        for p in data[3:-1]:
            self.points.append(parse_value(p))

    def total(self) -> int:
        return sum(self.points)

    def total_with_drops(self) -> int:
        self.sorted = sorted(self.points, reverse=True)
        self.best = self.sorted[:(RACES - DROPS)]
        return sum(self.best)

    def display(self, verbose=False) -> str:
        driver_total = f"\n{self.driver}\tTotal: {self.total()}\tWith Drops: {self.total_with_drops()}"
        if not verbose:
            return driver_total
        return (f"{driver_total}\n"
                f"Points {self.points}\n"
                f"Sorted {self.sorted}\n"
                f"Best {self.best}")


points = []
with open("sbrr-2026-points.csv") as file:
    rows = csv.reader(file)
    for _ in range(ROWS_TO_SKIP):
        next(rows)
    for row in rows:
        points.append(DriverPoints(row))

points.sort(key=lambda p: p.total_with_drops(), reverse=True)
for p in points:
    print(p.display(True))
