for _ in range(int(input())):
    N, K = map(int, input().split())
    print(sum(c // K for c in list(map(int, input().split()))))