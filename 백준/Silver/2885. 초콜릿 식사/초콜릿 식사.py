K = int(input())

for i in range(21):
    if K <= 2 ** i:
        choco = 2 ** i 
        break

tmp, cnt = choco, 0

if K != choco:
    while K:
        tmp //= 2

        if K >= tmp:
            K = K - tmp
            cnt += 1
        else:
            cnt += 1
            
print(choco, cnt)