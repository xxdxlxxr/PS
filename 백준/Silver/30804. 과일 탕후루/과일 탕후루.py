N, S = int(input()), list(map(int, input().split()))
answer, left, cnt, tmp = 0, 0, {}, 0

for right in range(N):
    if S[right] in cnt:
        cnt[S[right]] += 1
    else:
        cnt[S[right]] = 1
        tmp += 1

    while tmp > 2:
        cnt[S[left]] -= 1

        if cnt[S[left]] == 0:
            del cnt[S[left]]
            tmp -= 1

        left += 1

    answer = max(answer, right - left + 1)

print(answer)