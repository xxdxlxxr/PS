angle = [int(input()) for _ in range(3)]

print(['Error', 'Equilateral', 'Isosceles', 'Scalene'][(sum(angle) == 180) * len(set(angle))])