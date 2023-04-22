cups = [1, 0, 0, 2]

for change in input():
    i = ord(change) - 65
    cups[max(i - 1, 0) // 2], cups[min(i + 1 - 2 * (i >= 3), 3)] = cups[min(i + 1 - 2 * (i >= 3), 3)], cups[max(i - 1, 0) // 2]

print(cups.index(1) + 1)
print(cups.index(2) + 1)