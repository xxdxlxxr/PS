nums = sorted(list(map(int, input().split())))

print(1 if nums[0] + nums[1] == nums[2] else 2 if nums[0] * nums[1] == nums[2] else 3)