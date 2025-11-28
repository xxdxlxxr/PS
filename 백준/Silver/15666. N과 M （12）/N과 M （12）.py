def backtrack(start, arr):
    if len(arr) == M:
        print(*arr)
        return

    for i in range(start, len(nums)):
        backtrack(i, arr + [nums[i]])

N, M = map(int, input().split())
nums = sorted(set(map(int, input().split())))

backtrack(0, [])