N, nums, tmp = int(input()), [0] + list(map(int, input().split())), 0

for i in range(1, N):
    if i % 2 != 0 and nums[i] % 2 == 0:
        tmp += 1
        break
    elif i % 2 == 0 and nums[i] % 2 != 0:
        tmp += 1
        break

print('NO' if tmp > 0 else 'YES')