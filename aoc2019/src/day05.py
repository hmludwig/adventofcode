import intcode

f = open("../input/input05")
program = f.readline().split(",")
program = [int(i) for i in program]

intcode.run(program)
