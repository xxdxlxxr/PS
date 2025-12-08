def f_gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

nums = sorted([int(input()) for _ in range(int(input()))])
tmp = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
gcd, cnt = tmp[0], 0

for i in range(1, len(tmp)):
    gcd = f_gcd(gcd, tmp[i])

for j in tmp:
    cnt += j // gcd - 1

print(cnt)