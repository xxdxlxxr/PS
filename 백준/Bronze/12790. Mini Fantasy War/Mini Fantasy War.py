for _ in range(int(input())):
    nums = list(map(int, input().split()))

    print(max(1, nums[0] + nums[4]) + 5 * max(1, nums[1] + nums[5]) + 2 * (max(0, nums[2] + nums[6]) + nums[3] + nums[7]))