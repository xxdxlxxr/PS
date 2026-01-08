N, nums = int(input()), list(map(int, input().split()))
total = sum(nums)
answer = 0

for n in nums:
    total -= n
    answer += total * n

print(answer)