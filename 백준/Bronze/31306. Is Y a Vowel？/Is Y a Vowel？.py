cnt = [0, 0]

for char in input():
    if char in 'aeiou':
        cnt[0] += 1
    elif char == 'y':
        cnt[1] += 1

print(cnt[0], cnt[0] + cnt[1])