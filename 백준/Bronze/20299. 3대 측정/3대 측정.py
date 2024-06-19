N, K, L = map(int, input().split())
cnt, answer = 0, []

for _ in range(N):
    ratings = list(map(int, input().split()))

    if sum(rating >= L for rating in ratings) == 3 and sum(ratings) >= K:
        cnt += 1
        answer.extend(ratings)

print(cnt)
print(*answer)