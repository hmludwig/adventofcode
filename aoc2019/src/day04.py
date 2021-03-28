a = str(183564)
b = str(657474)

cnt1 = 0
cnt2 = 0

for i in range(int(a), int(b) + 1):
    adjacent = False
    decrease = False
    valid = False
    numbers = {}
    numbers[str(i)[0]] = 1
    for j in range(1, len(str(i))):
        prev = numbers.get(str(i)[j], 0)
        numbers[str(i)[j]] = prev + 1
        if str(i)[j - 1] == str(i)[j]:
            adjacent = True
        if str(i)[j - 1] > str(i)[j]:
            decrease = True
    if adjacent and not decrease:
        cnt1 += 1
        groups = {key: value for key, value in numbers.items() if value == 2}
        if len(groups) >= 1:
            cnt2 += 1
print(cnt1)
print(cnt2)
