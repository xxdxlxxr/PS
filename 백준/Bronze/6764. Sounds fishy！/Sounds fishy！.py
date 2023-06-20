nums = [int(input()) for _ in range(4)]

if len(set(nums)) == 1:
    print('Fish At Constant Depth')
elif len(set(nums)) == 4 and sorted(nums) == nums:
    print('Fish Rising')
elif len(set(nums)) == 4 and sorted(nums, reverse = True) == nums:
    print('Fish Diving')
else:
    print('No Fish')