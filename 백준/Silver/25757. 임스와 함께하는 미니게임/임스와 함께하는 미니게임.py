N, YFO = input().split()
print(len(set(input() for _ in range(int(N)))) // ('YFO'.index(YFO) + 1))