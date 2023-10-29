n, T = map(int, input().split())
nums = list(map(int, input().split()))
stack = 0

for i in range(n):
    stack += nums[i]

    if stack > T:
        print(i)
        break
    elif i == n - 1:
        print(n)