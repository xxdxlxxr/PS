n, k = map(int, input().split())
arr = [int(input()) for _ in range(k)]
tmp = answer = sum(arr[:k])

for i in range(n - k):
    arr.append(int(input()))

    tmp += arr[-1] - arr[i]
    answer = max(tmp, answer)

print(answer)