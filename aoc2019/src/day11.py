import intcode

f = open("../input/input11")
program = f.read().split(',')
program = [int(i) for i in program] 
halted = False 
pos = 0 
relative_base = 0

x = y = 0
orientation = 0  # 0: north, 1: east, 2: south, 3: west
start_color = 1
panel = {(x, y): start_color}

while not halted:
    program, pos, relative_base, halted, output = intcode.run(
        program, pos, [panel[(x, y)] if (x, y) in panel else [0]],
        relative_base)

    if output == []:
        break
    elif output[0] == 0:
        panel[(x, y)] = 0
    else:
        panel[(x, y)] = 1

    if output[1] == 0:
        if orientation == 0:
            orientation = 3
        else:
            orientation -= 1
    elif output[1] == 1:
        if orientation == 3:
            orientation = 0
        else:
            orientation += 1

    if orientation == 0:
        x -= 1
    elif orientation == 1:
        y += 1
    elif orientation == 2:
        x += 1
    elif orientation == 3:
        y -= 1

    if (x, y) not in panel:
        panel[(x, y)] = 0

print(len(panel))

min_x = min_y = 0
max_x = max_y = 0
for k, _ in panel.items():
    if k[0] > max_x:
        max_x = k[0]
    if k[0] < min_x:
        min_x = k[0]
    if k[1] > max_y:
        max_y = k[1]
    if k[1] < min_y:
        min_y = k[1]

picture = ['.'] * ((max_x + 1) * (max_y + 1))
print(max_x, max_y)

for k, v in panel.items():
    loc = max_y * k[0] + k[1] 
    picture[loc] = ' ' if v == 0 else '#'

counter = 0
for p in picture:
    if counter == max_y:
        counter = 0
        print()
    print(p, end='')
    counter += 1
print()
