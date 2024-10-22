import csv
from points_calculator import PointsCalculator


points = []
with open("sbrr-2024-points.csv", newline="") as file:
    rows = csv.reader(file)
    for row in rows:
        points.append(PointsCalculator(row))

points.sort(key=lambda p: p.total_with_drops(), reverse=True)
for p in points:
    print(p.display())
