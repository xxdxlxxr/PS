N, M, nums = int(input()), int(input()), sorted(list(map(int,input().split())))
left, right, cnt = 0, len(nums) - 1, 0

while left < right:
    sum_num = nums[left] + nums[right]

    if sum_num < M:
        left += 1
    elif sum_num > M:
        right -= 1
    else:
        cnt += 1
        left += 1
        right -= 1

print(cnt)