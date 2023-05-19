xs, ys, answer = [], [], 2 * [0]

for _ in range(3):
    x, y = map(int, input().split())

    xs.append(x)
    ys.append(y)

for i in range(3):
    if xs.count(xs[i]) == 1:
        answer[0] = xs[i]

    if ys.count(ys[i]) == 1:
        answer[1] = ys[i]

print(*answer)