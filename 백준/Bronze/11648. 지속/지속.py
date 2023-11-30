N, answer = int(input()), 0

while len(str(N)) > 1:
    answer += 1
    tmp = 1

    for num in str(N):
        tmp *= int(num)

    N = tmp

print(answer)