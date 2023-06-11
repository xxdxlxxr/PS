i = 1

while 1:
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        break

    if nums[0] % 2:
        answer = nums[1:][nums[0] // 2]
    else:
        answer = (nums[1:][nums[0] // 2 - 1] + nums[1:][nums[0] // 2]) / 2

    print(f'Case {i}: {answer:.1f}')

    i += 1