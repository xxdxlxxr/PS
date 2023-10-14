import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    print(int(n & -n == n))