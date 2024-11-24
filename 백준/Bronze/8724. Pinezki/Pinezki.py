n, cnt, answer = int(input()), 0, 0

for b in map(int, input().split()):
    if b:
        cnt += 1
    else:
        answer = max(cnt, answer)
        cnt = 0

print(max(cnt, answer))