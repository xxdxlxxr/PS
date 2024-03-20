answer = 4 * [0]

for _ in range(int(input())):
    G, C, N = map(int, input().split())

    if G == 1:
        answer[3] += 1
    else:
        answer[max(C, 2) - 2] += 1

for number in answer:
    print(number)