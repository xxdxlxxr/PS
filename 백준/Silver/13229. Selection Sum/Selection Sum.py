n, arr = int(input()), [0] + list(map(int, input().split()))

for i in range(1, n):
    arr[i + 1] += arr[i]

for _ in range(int(input())):
    start, end = map(int, input().split())

    print(arr[end + 1] - arr[start])