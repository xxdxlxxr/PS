singers, answer = {}, 0

for _ in range(int(input())):
    singer = input()

    if not singer in singers.keys():
        singers[singer] = 0

    singers[singer] += 1

for singer in singers.keys():
    answer += singers[singer] > 1

print(answer)