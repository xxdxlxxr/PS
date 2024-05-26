answer = 0

for _ in range(int(input())):
    P = input()
    answer += int(P[:-1]) ** int(P[-1])

print(answer)