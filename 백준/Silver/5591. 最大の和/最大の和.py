n, k = map(int, input().split())
arr = [int(input()) for _ in range(n)]
tmp = answer = sum(arr[:k])

for i in range(n - k):
    tmp += arr[i + k] - arr[i]
    answer = max(tmp, answer)

print(answer)