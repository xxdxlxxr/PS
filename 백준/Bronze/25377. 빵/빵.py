answer = 1001

for _ in range(int(input())):
    A, B = map(int, input().split())

    if A <= B:
        answer = min(answer, B)

print(-1 if answer == 1001 else answer)