AB = [0, 1]

for _ in range(int(input()) - 1):
    AB.append(AB[-2] + AB[-1])

print(AB[-2], AB[-1])