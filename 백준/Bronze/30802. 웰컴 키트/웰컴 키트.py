N, S = int(input()), map(int, input().split())
T, P = map(int, input().split())
print(sum(s // T + (s % T != 0) for s in S))
print(N // P, N % P)