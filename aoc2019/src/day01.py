f = open("../input/input01")
lines = f.read().splitlines()

sum1 = 0
for i in lines:
    sum1 += int(i) // 3 - 2

print(sum1)

sum2 = 0

for i in lines:
    subsum = int(i) // 3 - 2
    while subsum >= 0:
        sum2 += subsum
        subsum = subsum // 3 - 2

print(sum2)
