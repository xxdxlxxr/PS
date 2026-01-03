N, K = map(int, input().split())
wines = sorted([0] + list(map(int, input().split())))
prev, end, cnt, answer = 0, len(wines) - 1, 0, 0

while cnt < K:
    if cnt % 2:
        prev += 1
        cnt += 1
    else:
        answer += wines[end] - wines[prev]
        end -= 1
        cnt += 1

print(answer)