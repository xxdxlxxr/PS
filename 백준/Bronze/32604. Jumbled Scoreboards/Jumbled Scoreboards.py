tmp_t, tmp_p, answer = -1, -1, True

for _ in range(int(input())):
    a, b = map(int, input().split())

    if not answer:
        continue

    if tmp_t > a or tmp_p > b:
        answer = False
        continue

    tmp_t, tmp_p = a, b

print(['no', 'yes'][answer])