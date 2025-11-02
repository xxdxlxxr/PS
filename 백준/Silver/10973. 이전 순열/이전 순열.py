N, nums = int(input()), list(map(int, input().split()))

for i in range(N - 1, 0, -1):
    if nums[i] < nums[i-1]:
        x, y = i - 1, i

        for j in range(N - 1, 0, -1):
            if nums[j] < nums[x]:
                nums[j], nums[x] = nums[x], nums[j]
                nums = nums[:i] + sorted(nums[i:], reverse=True)
                print(*nums)
                exit(0)

print(-1)