def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

N, S = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N):
    A[i] = abs(S - A[i])

answer = A[0]

for i in range(1, N):
    answer = gcd(answer, A[i])

print(answer)