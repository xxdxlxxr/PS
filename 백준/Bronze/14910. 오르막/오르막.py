nums = list(map(int, input().split()))
answer = 1

for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        answer = 0
        break

print('Good' if answer else 'Bad')