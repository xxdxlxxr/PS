N, X = map(int, input().split())
arr = list(map(int, input().split()))
answer = tmp = sum(arr[:X])
cnt = 1

for i in range(N - X):
    tmp += arr[i + X] - arr[i]

    if tmp == answer:
        cnt += 1
    elif tmp > answer:
        answer, cnt = max(tmp, answer), 1

if answer:
    print(answer)
    print(cnt)
else:
    print('SAD')