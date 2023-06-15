t = [int(input()) for _ in range(2)]

while t[-2] >= t[-1]:
    t.append(t[-2] - t[-1])

print(len(t))