N, tmp, answer = int(input()), 0, 0

for rain in map(int, input().split()):
    tmp += 2 * rain - 1
    answer += tmp

print(answer)