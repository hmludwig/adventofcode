import sys

f = open(sys.argv[1])
data = f.read().strip().splitlines()
print(data)
print(data[0])
print(data[0][0])
