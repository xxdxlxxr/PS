N, tmp, answer = int(input()), 1, 1

while tmp < N:
    tmp += 6 * answer
    answer += 1

print(answer)