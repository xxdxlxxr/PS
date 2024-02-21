N, X, K = map(int, input().split())
arr = [i == X - 1 for i in range(N)]

for _ in range(K):
    A, B = map(int, input().split())
    arr[A - 1], arr[B - 1] = arr[B - 1], arr[A - 1]

print(arr.index(1) + 1)