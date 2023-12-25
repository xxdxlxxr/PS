answer = [0, 0]

for _ in range(int(input())):
    A, B = map(int, input().split())

    if A != B:
        answer[int((B - A) // abs(B - A) / 2 + .5)] += 1

print(*answer)