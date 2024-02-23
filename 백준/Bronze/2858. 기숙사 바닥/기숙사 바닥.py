R, B = map(int, input().split())

for i in range(1, B + 1):
    if B % i == 0 and R - 4 == 2 * (B // i + i):
        break

print(B // i + 2, i + 2)