def run(intcode, pos=0, data=None, relative_base=0):
    if len(intcode) < 100000:
        padding = [0] * 100000
        intcode += padding
    output = [] 
    halted = False
    j = 0
    op = intcode[pos] % 100
    data = [0] if data == None else data
    pair = 0
    while op != 99:
        op = intcode[pos] % 100
        if op == 99:
            halted = True
            break
        mode = intcode[pos] // 100
        mode1 = int(mode % 10)
        mode2 = int(mode % 100 / 10)
        mode3 = int(mode % 1000 / 100)

        if op == 1:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if mode3 == 0:
                intcode[intcode[pos + 3]] = a + b
            elif mode3 == 2:
                intcode[intcode[pos + 3] + relative_base] = a + b

            pos += 4

        elif op == 2:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if mode3 == 0:
                intcode[intcode[pos + 3]] = a * b
            elif mode3 == 2:
                intcode[intcode[pos + 3] + relative_base] = a * b

            pos += 4

        elif op == 3:
            if mode1 == 0:
                intcode[intcode[pos + 1]] = data[j]
            elif mode1 == 1:
                intcode[pos + 1] = data[j]
            elif mode1 == 2:
                intcode[intcode[pos + 1] + relative_base] = data[j]

            j += 1
            pos += 2

        elif op == 4:
            if mode1 == 0:
                output += [intcode[intcode[pos + 1]]]
            elif mode1 == 1:
                output += [intcode[pos + 1]]
            elif mode1 == 2:
                output += [intcode[intcode[pos + 1] + relative_base]]

            pos += 2
            pair += 1
            if pair == 2:
                pair = 0
                break

        elif op == 5:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if a:
                pos = b
            else:
                pos += 3

        elif op == 6:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if a == 0:
                pos = b
            else:
                pos += 3

        elif op == 7:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if a < b:
                if mode3 == 0:
                    intcode[intcode[pos + 3]] = 1
                elif mode3 == 2:
                    intcode[intcode[pos + 3] + relative_base] = 1
            else:
                if mode3 == 0:
                    intcode[intcode[pos + 3]] = 0
                elif mode3 == 2:
                    intcode[intcode[pos + 3] + relative_base] = 0

            pos += 4

        elif op == 8:
            if mode1 == 0:
                a = intcode[intcode[pos + 1]]
            elif mode1 == 1:
                a = intcode[pos + 1]
            elif mode1 == 2:
                a = intcode[intcode[pos + 1] + relative_base]

            if mode2 == 0:
                b = intcode[intcode[pos + 2]]
            elif mode2 == 1:
                b = intcode[pos + 2]
            elif mode2 == 2:
                b = intcode[intcode[pos + 2] + relative_base]

            if a == b:
                if mode3 == 0:
                    intcode[intcode[pos + 3]] = 1
                elif mode3 == 2:
                    intcode[intcode[pos + 3] + relative_base] = 1
            else:
                if mode3 == 0:
                    intcode[intcode[pos + 3]] = 0
                elif mode3 == 2:
                    intcode[intcode[pos + 3] + relative_base] = 0

            pos += 4

        elif op == 9:
            if mode1 == 0:
                relative_base += intcode[intcode[pos + 1]]
            elif mode1 == 1:
                relative_base += intcode[pos + 1]
            elif mode1 == 2:
                relative_base += intcode[intcode[pos + 1] + relative_base]

            pos += 2
        else:
            break
    
    return (intcode, pos, relative_base, halted, output)
