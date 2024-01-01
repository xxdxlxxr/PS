C, answer = int(input()), 1

while C > 1:
    C = 3 * C + 1 if C % 2 else C / 2
    answer += 1

print(answer)