nums = [list(map(int, input().split())) for _ in range(int(input()))]
tmp, answer = [0 for _ in range(10 ** 6 + 1)], 0

for a, b, c in nums:
    if not tmp[a] and not tmp[b] and not tmp[c]:
        answer += 1

    tmp[a], tmp[b], tmp[c] = 1, 1, 1

print(answer)