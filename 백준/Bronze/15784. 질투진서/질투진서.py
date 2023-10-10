N, a, b = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print('ANGRY' if sum(num > arr[a - 1][b - 1] for num in [nums[b - 1] for nums in arr] + arr[a - 1]) else 'HAPPY')