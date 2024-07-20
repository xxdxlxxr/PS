import sys

inputs, nums = sys.stdin.readlines(), []

for i in range(len(inputs)):
    nums += map(int, ''.join(reversed(inputs[i].strip('\n'))).split())

    if not i:
        nums.pop()

for num in sorted(nums):
    print(num)