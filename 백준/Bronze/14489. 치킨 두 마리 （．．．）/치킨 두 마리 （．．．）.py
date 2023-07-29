AB = sum(map(int, input().split()))
C = 2 * int(input())

print(AB - (AB >= C) * C)