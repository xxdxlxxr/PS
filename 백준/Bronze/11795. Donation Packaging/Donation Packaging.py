answer = [0, 0, 0]

for _ in range(int(input())):
    a, b, c = map(int, input().split())
    answer[0] += a
    answer[1] += b
    answer[2] += c

    if answer[0] < 30 or answer[1] < 30 or answer[2] < 30:
        print("NO")
    else:
        d = min(answer)
        print(d)
        answer[0] -= d
        answer[1] -= d
        answer[2] -= d