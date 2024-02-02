N = int(input())
arr = [int(input()) for _ in range(N)]

print(2 * arr[-1] - arr[-2] if arr[0] + arr[2] == 2 * arr[1] else arr[-1] ** 2 // arr[-2])