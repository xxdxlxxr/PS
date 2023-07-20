import sys

input = sys.stdin.readline

N, Q = map(int, input().split())
A = [0] + sorted(map(int, input().split()))

for i in range(1, N):
    A[i + 1] += A[i]

for _ in range(Q):
    L, R = map(int, input().split())

    print(A[R] - A[L - 1])