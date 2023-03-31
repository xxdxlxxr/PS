n, t = int(input()), [1]

for i in range(n):
    sum = 0

    for j in range(i + 1):
        sum += t[j] * t[i - j]

    t.append(sum)

print(t[-1])