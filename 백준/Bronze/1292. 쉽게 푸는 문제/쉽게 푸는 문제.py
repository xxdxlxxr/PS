A, B = map(int, input().split())
arr = [0]

for i in range(1, 46):
    arr += i * [i]

for i in range(len(arr) - 1):
    arr[i + 1] += arr[i]

print(arr[B] - arr[A - 1])