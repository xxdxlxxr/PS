answer = [0, 0]

for i in range(9):
    n = int(input())

    if answer[0] < n:
        answer[0], answer[1] = n, i + 1

print(answer[0])
print(answer[1])