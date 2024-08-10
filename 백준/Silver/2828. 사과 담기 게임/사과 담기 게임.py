N, M = map(int, input().split())
cur, answer = 1, 0

for _ in range(int(input())):
    loc = int(input())

    if cur > loc:
        answer += cur - loc
        cur = loc
    elif cur + M < loc + 1:
        answer += loc - cur - M + 1
        cur = loc - M + 1

print(answer)