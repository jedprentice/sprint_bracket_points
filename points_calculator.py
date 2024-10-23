import csv

DROPS = 8
RACES = 25
RANDOM_EMPTY_COLUMNS = [8, 17]


def parse_value(s: str) -> int:
    if s == "":
        return 0
    return int(s)


class DriverPoints:
    def __init__(self, data: list[str]):
        del data[RANDOM_EMPTY_COLUMNS[0]]
        del data[RANDOM_EMPTY_COLUMNS[1] - 1]
        self.driver = data[0]
        self.points = []
        for p in data[3:]:
            self.points.append(parse_value(p))

    def total(self) -> int:
        return sum(self.points)

    def total_with_drops(self) -> int:
        self.sorted = sorted(self.points, reverse=True)
        self.best = self.sorted[:(RACES - DROPS)]
        return sum(self.best)

    def display(self) -> str:
        return (f"\n{self.driver}\t Total: {self.total()}\t"
                f"With Drops: {self.total_with_drops()}\n"
                f"Points {self.points}\n"
                f"Sorted {self.sorted}\n"
                f"Best {self.best}")


points = []
with open("sbrr-2024-points.csv") as file:
    rows = csv.reader(file)
    for row in rows:
        points.append(DriverPoints(row))

points.sort(key=lambda p: p.total_with_drops(), reverse=True)
for p in points:
    print(p.display())
