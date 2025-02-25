answer = -1

for _ in range(int(input())):
    A, B = map(int, input().split())

    if A <= B:
        answer = min(answer, B)

print(answer)