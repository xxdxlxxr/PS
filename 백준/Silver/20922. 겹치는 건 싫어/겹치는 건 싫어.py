from collections import defaultdict

N, K = map(int,input().split())
a = list(map(int,input().split()))
left, right, tmp, answer = 0, 0, defaultdict(int), 0

while 1:
    if right == N:
        break

    if tmp[a[right]] < K:
        tmp[a[right]] += 1
        right += 1
    else:
        tmp[a[left]] -= 1
        left += 1

    answer = max(right - left, answer)

print(answer)