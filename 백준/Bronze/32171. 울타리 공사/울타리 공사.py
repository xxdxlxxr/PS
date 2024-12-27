tmp = [10, 10, -10, -10]

for _ in range(int(input())):
    a, b, c, d = map(int, input().split())
    tmp = [min(tmp[0], a), min(tmp[1], b), max(tmp[2], c), max(tmp[3], d)]
    print(2 * (sum(tmp[2:]) - sum(tmp[:2])))