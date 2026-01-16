from itertools import permutations

X, Y, answer = [], [], 1e9

for _ in range(4):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

for permutation in permutations([1, 2, 3], 3):
    x, y, move = X[0], Y[0], 0

    for i in permutation:
        move += (abs(x - X[i]) ** 2 + abs(y - Y[i]) ** 2) ** 0.5
        x = X[i]
        y = Y[i]
        
    answer = min(answer, int(move))
        
print(answer)