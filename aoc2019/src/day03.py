f = open("../input/input03")
lines = f.read().splitlines()
wire1 = lines[0].split(",")
wire2 = lines[1].split(",")


def getPathCoordinates(path):
    directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
    points = {}
    posx = posy = step = 0
    for move in path:
        dx, dy = directions[move[0]]
        for _ in range(int(move[1:])):
            posx += dx
            posy += dy
            step += 1
            if (posx, posy) not in points:
                points[(posx, posy)] = step
    return points


wire1Coordinates = getPathCoordinates(wire1)
wire2Coordinates = getPathCoordinates(wire2)
intersectionPoints = [
    point for point in wire1Coordinates if point in wire2Coordinates
]

print(wire1Coordinates)
print(wire2Coordinates)
print(min(abs(x) + abs(y) for (x, y) in intersectionPoints))
print(
    min(wire1Coordinates[point] + wire2Coordinates[point]
        for point in intersectionPoints))
