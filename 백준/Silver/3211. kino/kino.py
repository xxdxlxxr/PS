N = int(input())
arr = sorted(int(input()) for _ in range(N))

for i in range(N):
    if arr[i] < i + 1:
        print(i + 1)
        break