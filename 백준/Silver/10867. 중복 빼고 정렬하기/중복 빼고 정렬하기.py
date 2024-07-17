N, nums = int(input()), sorted(map(int, input().split())) + [1001]
print(*(nums[i] for i in range(N) if nums[i] != nums[i + 1]))