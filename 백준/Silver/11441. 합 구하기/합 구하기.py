N = int(input())
A = [0] + list(map(int, input().split()))

for i in range(N):
    A[i + 1] += A[i]

for _ in range(int(input())):
    i, j = map(int, input().split())

    print(A[j] - A[i - 1])