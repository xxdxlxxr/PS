for _ in range(int(input())):
    scores, cnt = list(map(int, input().split())), 0

    for score in scores[1:]:
        if score > sum(scores[1:]) / scores[0]:
            cnt += 1

    print(f'{100 * cnt / scores[0]:.3f}%')