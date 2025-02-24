ABC = [0] + list(map(int, input().split()))
tmp, answer = 101 * [0], 0

for _ in range(3):
    a, b = map(int, input().split())

    for i in range(a, b):
        tmp[i] += 1

print(sum(cnt * ABC[cnt] for cnt in tmp))