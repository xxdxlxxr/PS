N, M, B = map(int, input().split())
block, tmp, answer = [[int(height) for height in input().split()] for _ in range(N)], 0, int(1e9)

for i in range(257):
    use_block = 0
    take_block = 0

    for x in range(N):
        for y in range(M):
            if block[x][y] > i:
                take_block += block[x][y] - i
            else:
                use_block += i - block[x][y]

    if use_block > take_block + B:
        continue

    cnt = 2 * take_block + use_block

    if cnt <= answer:
        answer = cnt
        tmp = i

print(answer, tmp)