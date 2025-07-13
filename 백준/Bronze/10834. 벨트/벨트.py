rot, answer = 0, 0

for i in range(int(input())):
    a, b, r = map(int, input().split())

    if i == 0:
        answer = a * b
    else:
        answer = int(answer / a * b)

    if r == 1:
        rot = 1 - rot

print(rot, answer)