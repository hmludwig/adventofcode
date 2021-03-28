f = open("../input/input08")
data = f.readline().strip('\n')
data = [int(x) for x in data]
WIDTH = 25
HEIGHT = 6

layers = [
    data[i:i + WIDTH * HEIGHT] for i in range(0, len(data), WIDTH * HEIGHT)
]

min_layer = 0
for i in range(len(layers)):
    if layers[min_layer].count(0) >= layers[i].count(0):
        min_layer = i

print(layers[min_layer].count(1) * layers[min_layer].count(2))

picture = [int(-1) for _ in range(WIDTH * HEIGHT)]

for layer in layers:
    for i in range(len(layer)):
        if picture[i] != -1 or layer[i] == 2:
            continue
        else:
            picture[i] = layer[i]

for i in range(WIDTH * HEIGHT):
    if (i % 25 == 0):
        print()
    if picture[i] == 0:
        print(' ', end='')
    else:
        print(picture[i], end='')
print()
