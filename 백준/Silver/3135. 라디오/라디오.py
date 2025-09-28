A, B = map(int, input().split())
favorites, tmp1, tmp2 = [int(input()) for _ in range(int(input()))], [abs(A - B)], []

for i in range(len(favorites)):
    tmp2.append(abs(favorites[i] - B))

print(min(tmp1) if min(tmp1) <= min(tmp2) else min(tmp2) + 1)