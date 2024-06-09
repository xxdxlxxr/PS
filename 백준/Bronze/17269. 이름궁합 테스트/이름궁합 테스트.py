N, M = map(int, input().split())
A, B = input().split()
AB = ''.join(a + b for a, b in zip(A, B))

if N - M:
    AB += [A, B][N < M][-(max(N, M) - min(N, M)):]

answer = [[3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1][ord(char) - ord('A')] for char in AB]

for i in range(N + M - 2):
    for j in range(N + M - i - 1):
        answer[j] = (answer[j] + answer[j + 1]) % 10

print(str(int(''.join(map(str, answer[:2])))) + '%')