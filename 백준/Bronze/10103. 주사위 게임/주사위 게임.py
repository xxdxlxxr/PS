c, s = 100, 100

for _ in range(int(input())):
    a, b = map(int, input().split())

    if a < b:
        c -= b
    elif a > b:
        s -= a

print(c)
print(s)