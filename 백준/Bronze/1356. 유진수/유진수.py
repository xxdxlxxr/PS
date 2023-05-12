N, answer = list(input()), 'NO'
length = len(N)

for i in range(length - 1):
    left, right = 1, 1

    for j in map(int, N[:i + 1]):
        left *= j

    for k in map(int, N[i + 1:]):
        right *= k

    if left == right:
        answer = 'YES'
        break

print(answer)