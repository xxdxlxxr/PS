N, M = map(int, input().split())
arr = N * [0]

for _ in range(M):
    A, B = map(int, input().split())

    arr[A - 1] += 1
    arr[B - 1] += 1

for number in arr:
    print(number)