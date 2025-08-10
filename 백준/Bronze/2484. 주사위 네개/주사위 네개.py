def func(nums):
    if len(set(nums)) == 1:
        return 50000 + nums[0] * 5000

    if len(set(nums)) == 2:
        if nums[1] == nums[2]:
            return 10000 + nums[1] * 1000
        else:
            return 2000 + nums[0] * 500 + nums[2] * 500

    for i in range(3):
        if nums[i] == nums[i+1]:
            return 1000 + nums[i] * 100

    return nums[3] * 100

print(max(func(sorted(list(map(int, input().split())))) for _ in range(int(input()))))