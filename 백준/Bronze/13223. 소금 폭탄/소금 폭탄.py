current, drop = list(map(int, input().split(':'))), list(map(int, input().split(':')))
answer = sum(60 ** (2 - i) * drop[i] for i in range(3)) - sum((60 ** (2 - i)) * current[i] for i in range(3))

if answer <= 0:
    answer += 24 * 60 ** 2

print(str(answer // 60 ** 2).zfill(2), str(answer % 60 ** 2 // 60).zfill(2), str(answer % 60).zfill(2), sep=':')