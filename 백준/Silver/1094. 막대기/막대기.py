X, stick, answer = int(input()), [64, 32, 16, 8, 4, 2, 1], 0

for i in range(len(stick)):
    if X >= stick[i]:
        answer += 1
        X -= stick[i]

    if X == 0:
        break

print(answer)