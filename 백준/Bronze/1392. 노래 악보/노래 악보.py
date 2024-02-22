N, Q = map(int, input().split())
arr = []

for i in range(N):
    arr += int(input()) * [i + 1]

for _ in range(Q):
    print(arr[int(input())])