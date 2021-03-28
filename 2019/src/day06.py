from collections import defaultdict, deque

f = open("../input/input06").read().splitlines()
orbits = defaultdict(list)
connections = defaultdict(list)

for entry in f:
    i, j = entry.split(')')
    orbits[i].append(j)
    connections[i].append(j)
    connections[j].append(i)

def count_orbits(obj):
    if obj not in orbits:
        return 0
    children = orbits[obj]
    return len(children) + sum([count_orbits(i) for i in children])

print(sum([count_orbits(i) for i in orbits.keys()]))

def path(start, end):
    distances = {start: 0}
    objects = deque([start])
    seen = {start}
    while end not in distances:
        thing = objects.pop()
        distance = distances[thing]
        for neighbor in connections[thing]:
            if neighbor in seen:
                continue
            seen.add(neighbor)
            objects.appendleft(neighbor)
            distances[neighbor] = distance + 1
    return distances[end]

you_parent = [k for k, v in orbits.items() if 'YOU' in v].pop()
san_parent = [k for k, v in orbits.items() if 'SAN' in v].pop()
print(path(you_parent, san_parent))
