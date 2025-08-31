N, answer = int(input()), False

for i in range(2, 10):
    if not answer:
        for j in range(1, 10):
            if N in (i, j, i * j):
                answer = True
                break
    else:
        break

print(int(answer))