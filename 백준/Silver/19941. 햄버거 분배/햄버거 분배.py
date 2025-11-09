N, K = map(int, input().split())
string, answer = list(input()), 0

for i in range(N):
    if string[i] == 'P':
        for j in range(max(i - K, 0), min(i + K + 1, N)):
            if string[j] == 'H':
                string[j] = 0
                answer += 1
                break

print(answer)