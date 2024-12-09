answer = 0

for _ in range(int(input())):
    a, d, g = map(int, input().split())
    answer = max(((a == d + g) + 1) * a * (d + g), answer)

print(answer)