import sys

h, m, s = map(int, input().split())

for _ in range(int(input())):
    query = list(map(int, sys.stdin.readline().split()))

    if query[0] < 3:
        s += (3 - 2 * query[0]) * query[1]
    else:
        m += s // 60
        s %= 60
        h += m // 60
        m %= 60

        print(h % 24, m, s)