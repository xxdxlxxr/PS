U, N = map(int,input().split())
tmp_1, tmp_2, m = [[] for _ in range(10001)], [0 for _ in range(10001)], 10001

for _ in range(N):
    S, P = input().split()
    P = int(P)
    tmp_1[P].append(S)
    tmp_2[P] += 1

for i in range(10001): 
    if tmp_2[i] != 0:
        m = min(tmp_2[i], m)

for i in range(10001):
    if m == tmp_2[i]:
        print(tmp_1[i][0], i)
        break