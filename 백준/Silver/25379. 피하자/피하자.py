N = int(input())
cnt_odd, cnt_even, left_odd, left_even = 0, 0, 0, 0

for i in map(int, input().split()):
    if i % 2 == 1:
        cnt_odd += 1
        left_odd += cnt_even
    else:
        left_even += cnt_odd
        cnt_even += 1

print(min(left_even, left_odd))