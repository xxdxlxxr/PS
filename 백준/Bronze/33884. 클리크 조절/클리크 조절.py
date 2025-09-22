import sys

input = sys.stdin.readline
N = int(input())
first, second = [list(map(int, input().split())) for _ in range(N)], [list(map(int, input().split())) for _ in range(N)]
first.sort(key=lambda x: (x[0], x[1]))
second.sort(key=lambda x: (x[0], x[1]))
print(second[0][0] - first[0][0], second[0][1] - first[0][1])