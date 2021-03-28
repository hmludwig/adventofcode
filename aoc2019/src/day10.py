import math

f = open("../input/input10")
data = f.read().split()

asteroids_coords = [(x, y)
                    for y, row in enumerate(data)
                    for x, value in enumerate(row)
                    if value == '#']

max_asteroids = 0
monitoring_station = (0, 0)
for x, y in asteroids_coords:
    asteroids = set()
    for x2, y2 in asteroids_coords:
        if not (x == x2 and y == y2):
            dx, dy = x2 - x, y2 - y
            dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
            asteroids.add((dx, dy))
    if len(asteroids) > max_asteroids:
        max_asteroids = len(asteroids)
        monitoring_station = (x, y)

print(max_asteroids)

vaporized = [monitoring_station]
while len(vaporized) != len(asteroids_coords):
    closest_points = {}
    for x, y in asteroids_coords:
        if (x, y) not in vaporized:
            dx, dy = x - monitoring_station[0], y - monitoring_station[1]
            dx, dy = dx // math.gcd(dx, dy), dy // math.gcd(dx, dy)
            cx, cy = closest_points.get((dx, dy), (float('inf'), float('inf')))
            if abs(x - monitoring_station[0]
                  ) + abs(y - monitoring_station[1]) < abs(
                      cx - monitoring_station[0]) + abs(cy -
                                                        monitoring_station[1]):
                closest_points[(dx, dy)] = (x, y)
    vaporized += sorted(closest_points.values(),
                        key=lambda p: -math.atan2(p[0] - monitoring_station[0],
                                                  p[1] - monitoring_station[1]))

print(vaporized[200][0] * 100 + vaporized[200][1])
