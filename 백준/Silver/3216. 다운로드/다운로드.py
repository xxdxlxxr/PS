tmp, answer = 0, 0

for D, V in [list(map(int, input().split())) for _ in range(int(input()))]:
    tmp -= V

    if tmp < 0:
        answer -= tmp
        tmp = 0

    tmp += D

print(answer)