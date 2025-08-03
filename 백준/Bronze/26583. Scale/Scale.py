import sys

while 1:
    nums = sys.stdin.readline()

    if nums == '':
        break

    nums = [1] + list(map(int, nums.split())) + [1]

    print(* (nums[i - 1] * nums[i] * nums[i + 1] for i in range(1, len(nums) - 1)))