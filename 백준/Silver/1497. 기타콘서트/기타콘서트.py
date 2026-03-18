def bt(idx, guitar_cnt, song):
    global answer

    if idx == N or guitar_cnt > answer:
        return
    
    if song | guitars[idx][1] == tmp:
        answer = min(answer, guitar_cnt + 1)
        return
    
    bt(idx + 1, guitar_cnt + 1, song | guitars[idx][1])
    bt(idx + 1, guitar_cnt, song)

N, M = map(int, input().split())
guitars, tmp, answer = [], 0, int(1e9)

for _ in range(N):
    name, songs = input().split()
    binary = ''

    for song in songs:
        binary += '1' if song == 'Y' else '0'
        
    guitars.append((name, int(binary, 2)))
    tmp |= int(binary, 2)

bt(0, 0, 0)
print(answer if tmp != 0 else -1)