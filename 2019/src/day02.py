f = open("../input/input02")
program = f.readline().split(",")
program = [int(i) for i in program]


def runIntcode(intcode, a, b):
    intcode[1] = a
    intcode[2] = b
    for i in range(0, len(intcode), 4):
        if intcode[i] == 99:
            break
        elif intcode[i] == 1:
            intcode[intcode[i +
                            3]] = intcode[intcode[i + 1]] + intcode[intcode[i +
                                                                            2]]
        elif intcode[i] == 2:
            intcode[intcode[i +
                            3]] = intcode[intcode[i + 1]] * intcode[intcode[i +
                                                                            2]]
    return intcode


print(runIntcode(program.copy(), 12, 2)[0])

for i in range(100):
    for j in range(100):
        if runIntcode(program.copy(), i, j)[0] == 19690720:
            print(i, j)
            print(100 * i + j)
