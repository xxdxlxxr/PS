n = int(input())
A = [int(input()) for _ in range(n)]
B = [num ** 2 for num in A]
answer = 0

for i in range(n - 1):
    A[-(i + 2)] += A[-(i + 1)]
    B[i + 1] += B[i]

for i in range(n - 1):
    answer = max(B[i] * A[i + 1], answer)

print(answer)