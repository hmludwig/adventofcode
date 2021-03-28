import itertools

f = open("../input/input12")
data = f.read().split('\n')
data = [
    x.replace('<', '').replace(',', '').replace('>', '').split() for x in data
]


class Moon:

    def __init__(self, name, x, y, z):
        self.name = name
        self.position = (x, y, z)
        self.velocity = (0, 0, 0)
        self.pot = sum(map(abs, self.position))
        self.kin = abs(self.position[0] * self.position[1] * self.position[2])
        self.energy = self.pot + self.kin

    def __str__(self):
        return f'{self.name}: pos = {self.position}, vel = {self.velocity}'

    def __repr__(self):
        return f'{self.name}'

    def update(self):
        self.postion += self.velocity
        self.pot = sum(map(abs, self.position))
        self.kin = abs(self.position[0] * self.position[1] * self.position[2])
        self.energy = self.pot + self.kin


Io = Moon('Io', int(data[0][0][2:]), int(data[0][1][2:]), int(data[0][2][2:]))
Europa = Moon('Europa', int(data[1][0][2:]), int(data[1][1][2:]),
              int(data[1][2][2:]))
Ganymede = Moon('Ganymede', int(data[2][0][2:]), int(data[2][1][2:]),
                int(data[2][2][2:]))
Callisto = Moon('Callisto', int(data[3][0][2:]), int(data[3][1][2:]),
                int(data[3][2][2:]))

print(Io)
print(Europa)
print(Ganymede)
print(Callisto)

moons = [Io, Europa, Ganymede, Callisto]
combs = list(itertools.combinations(moons, 2))

for i in range(1000):
    change = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0, 0)]

