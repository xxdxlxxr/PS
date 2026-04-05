N1, N2 = map(int, input().split())
ant1, ant2 = list(reversed(input())), list(input())
answer = ant1 + ant2

for _ in range(int(input())):
    for i in range(len(answer) - 1):
        if answer[i] in ant1 and answer[i + 1] in ant2:
            answer[i], answer[i + 1] = answer[i + 1], answer[i]

            if answer[i + 1] == ant1[-1]:
                break

print(''.join(answer))