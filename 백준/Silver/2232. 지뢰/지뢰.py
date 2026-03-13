N = int(input())
nums = [0] + [int(input()) for _ in range(N)] + [0]
print('\n'.join(map(str, (i for i in range(1, N + 1) if nums[i - 1] <= nums[i] >= nums[i + 1]))))