distance = int(input())
length, answer = len(str(distance)), 0

for i in range(length):
    tmp = distance % 10
    distance //= 10

    if tmp > 4:
        answer += 9 ** i * (tmp - 1)
    else:
        answer += 9 ** i * tmp

print(answer)