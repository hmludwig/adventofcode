import intcode

f = open("../input/input09")
program = f.readline().split(",")
program = [int(i) for i in program] 

_, _, _, output = intcode.run(program, 0, [1])
print(output)

_, _, _, output = intcode.run(program, 0, [2])
print(output)
