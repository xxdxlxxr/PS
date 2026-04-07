N, tmp, answer = int(input()), 100001 * [0], 0

for i in range(N):
    tmp[int(input())] = i + 1

for i in range(1, N):
    if tmp[i] > tmp[i + 1]:
        answer += 1

print(answer)