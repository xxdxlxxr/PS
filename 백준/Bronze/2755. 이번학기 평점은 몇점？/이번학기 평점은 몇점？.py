sum = total = 0

for _ in range(int(input())):
    inputs = input().split()
    sum += int(inputs[1])

    if inputs[2] != 'F':
        total += int(inputs[1]) * (69 - ord(inputs[2][0]) + .3 * ('-0+'.index(inputs[2][1]) - 1))

print("%.2f" % round(total / sum + 10 ** -10, 2) if sum else 0.00)