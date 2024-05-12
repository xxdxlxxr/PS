fruits = {}

for _ in range(int(input())):
    S, X = input().split()

    if S not in fruits.keys():
        fruits[S] = 0

    fruits[S] += int(X)

print('YES' if 5 in fruits.values() else 'NO')