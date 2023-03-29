names = []

for _ in range(int(input())):
    name, d, m, y = input().split()

    names.append([y, int(m), int(d), name])

names.sort()

print(names[-1][3])
print(names[0][3])