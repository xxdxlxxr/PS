A, B, AB = input(), input(), ''
answer = [i * [0] for i in range(16, 1, -1)]

for i in range(8):
    answer[0][2 * i], answer[0][2 * i + 1] = int(A[i]), int(B[i])

for i in range(14):
    for j in range(15 - i):
        answer[i + 1][j] = (answer[i][j] + answer[i][j + 1]) % 10

print(answer[-1][0], answer[-1][1], sep = '')