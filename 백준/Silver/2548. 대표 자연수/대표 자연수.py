N, nums = int(input()), sorted(list(map(int, input().split())))
print(nums[len(nums) // 2 if len(nums) % 2 != 0 else (len(nums) // 2) - 1])