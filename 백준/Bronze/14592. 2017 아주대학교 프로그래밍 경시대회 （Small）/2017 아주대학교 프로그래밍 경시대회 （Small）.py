SCL = [list(map(int, input().split())) for _ in range(int(input()))]
sorted_SCL = sorted(SCL, key=lambda x:(-x[0], x[1], x[2]))
print(SCL.index(sorted_SCL[0]) + 1)