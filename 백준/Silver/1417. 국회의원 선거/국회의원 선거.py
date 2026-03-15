N, tmp = int(input()), int(input())
nums, answer = [int(input()) for _ in range(N - 1)], 0

if N == 1:
    pass
else:
    while tmp <= max(nums):
        tmp += 1
        answer += 1
        nums[nums.index(max(nums))] -= 1

print(answer)