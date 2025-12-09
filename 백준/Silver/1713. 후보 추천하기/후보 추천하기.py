N, vote, recommend = int(input()), int(input()), list(map(int, input().split()))
picture, score = [], []

for i in range(vote):
    if recommend[i] in picture:
        for j in range(len(picture)):
            if recommend[i] == picture[j]:
                score[j] += 1
    else:
        if len(picture) >= N:
            for j in range(N):
                if score[j] == min(score):
                    del picture[j]
                    del score[j]
                    break

        picture.append(recommend[i])
        score.append(1)

print(*sorted(picture))