import intcode, itertools

f = open("../input/input07")
program = f.readline().split(",")
program = [int(i) for i in program] 
thruster_signal_1 = 0
for phase in itertools.permutations(range(5)):
    prev = 0
    for i in range(5):
        data = [phase[i], prev]
        _, _, _, prev = intcode.run(program, 0, data)
    thruster_signal_1 = max(thruster_signal_1, prev)

print(thruster_signal_1)

thruster_signal_2 = 0
for phase in itertools.permutations(range(5, 10)):
    programs = []
    for i in range(5):
        programs.append(program.copy())
    positions = [0] * 5
    halted = [False] * 5
    loopback = False
    prev = 0
    while False in halted:
        for i in range(5):
            if not loopback:
                data = [phase[i], prev]
            else:
                data = [prev]
            programs[i], positions[i], halted[i], prev = intcode.run(
                programs[i], positions[i], data)
        loopback = True
    thruster_signal_2 = max(thruster_signal_2, prev)

print(thruster_signal_2)
