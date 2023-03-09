N = int(input())
A = list(map(int, input().split()))
result = N * [0]
skip = 0

for i in range(N):
    if not A[i]:
        skip += 1
    else:
        result[A[i] - 1] += 1

if result.count(max(result)) > 1:
    print('skipped')
else:
    print(result.index(max(result)) + 1)