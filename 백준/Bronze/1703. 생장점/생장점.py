while 1:
    nums = list(map(int, input().split()))
    answer = 1

    if len(nums) == 1:
        break

    for i in range(nums[0]):
        answer = answer * nums[2 * i + 1] - nums[2 * i + 2]

    print(answer)