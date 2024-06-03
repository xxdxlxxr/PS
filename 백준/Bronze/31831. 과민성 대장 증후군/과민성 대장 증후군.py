N, M = map(int, input().split())
A, stress, answer = list(map(int, input().split())), [0], 0

for i in range(N):
    stress.append(max(stress[-1] + A[i], 0))
    answer += stress[-1] >= M

print(answer)