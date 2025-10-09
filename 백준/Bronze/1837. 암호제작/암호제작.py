P, K = map(int,input().split())
cnt = 2

for i in range(2, K):
    if P % i == 0:
        p = i
        print("BAD", p)
        break
    else:
        cnt += 1

if cnt == K:
  print("GOOD")