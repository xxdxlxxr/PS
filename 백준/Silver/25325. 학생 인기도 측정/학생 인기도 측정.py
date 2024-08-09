n, cnt = int(input()), {name: 0 for name in input().split()}

for _ in range(n):
    for name in input().split():
        cnt[name] += 1

for k, v in sorted(cnt.items(), key=lambda x: x[1] , reverse=True):
    print(k, v)