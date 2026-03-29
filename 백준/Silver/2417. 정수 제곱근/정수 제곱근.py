n = int(input())
e, q = n, 0

while q <= e:
    mid = (q + e) // 2
    
    if mid ** 2 < n:
        q = mid + 1
    else:
        e = mid - 1

print(q)