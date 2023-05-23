answer = [0, 0]

for _ in range(int(input())):
    A, B = map(int, input().split())

    if A == B:
        answer[0] += A
        answer[1] += A
    else:
        answer[A < B] += A + B

print(*answer)