g, p, t = map(int, input().split())
s1, s2 = g * p, g + p * t
print(1 if s1 < s2 else 2 if s1 > s2 else 0)