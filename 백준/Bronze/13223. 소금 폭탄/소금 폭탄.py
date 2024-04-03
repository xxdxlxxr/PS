current, drop = list(map(int, input().split(':'))), list(map(int, input().split(':')))
answer = sum(60 ** (2 - i) * drop[i] for i in range(3)) - sum((60 ** (2 - i)) * current[i] for i in range(3))

if answer <= 0:
    answer += 24 * 60 ** 2

print('%02d:%02d:%02d' % (answer // 60 ** 2, answer % 60 ** 2 // 60, answer % 60))