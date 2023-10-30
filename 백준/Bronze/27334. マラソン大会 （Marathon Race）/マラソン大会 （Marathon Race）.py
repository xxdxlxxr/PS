N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    print(sorted(A).index(A[i]) + 1)