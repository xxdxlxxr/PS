N, ATK = map(int, input().split())
HP = 0
CurHP = 0
damage = 0
tah = []

for _ in range(N):
    tah.append(list(map(int, input().split())))

for i in tah:
    if i[0] == 1:
        cnt = i[2] % ATK

        if cnt:
            damage = -(i[1] * (i[2] // ATK))
        else:
            damage = -(i[1] * (i[2] // ATK - 1))
    else:
        ATK += i[1]
        damage = i[2]

    CurHP += damage

    if CurHP > 0:
        CurHP = 0

    HP = max(HP, abs(CurHP))

print(HP + 1)