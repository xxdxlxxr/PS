a, b, a_tot, b_tot, cnt = list(map(int, input().split())), list(map(int, input().split())), 0, 0, 0

for i in range(9):
    a_tot += a[i]

    if a_tot > b_tot and cnt == 0:
        cnt += 1

    if a_tot < b_tot and cnt == 1:
        cnt += 1

    b_tot += b[i]

print('Yes' if cnt == 2 and a_tot < b_tot or cnt == 1 and a_tot < b_tot else 'No')