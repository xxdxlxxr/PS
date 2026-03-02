N, tmp, cnt = int(input()), 1, 10 * [0]

while N != 0:
    while N % 10 != 9:
        for i in str(N):
            cnt[int(i)] += tmp
            
        N -= 1
        
    if N < 10:
        for i in range(N + 1):
            cnt[i] += tmp
            
        cnt[0] -= tmp
        break
    else:
        for i in range(10):
            cnt[i] += (N // 10 + 1) * tmp
            
    cnt[0] -= tmp
    tmp *= 10
    N //= 10

print(sum(cnt) % 1234567)