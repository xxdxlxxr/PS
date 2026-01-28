N, new_score, P = map(int, input().split())

if N:
    score_list = sorted(list(map(int, input().split())) + [new_score], reverse=True)

    if P >= (score_list.index(new_score) + 1):
        if N == P and new_score <= score_list[-1]:
            print(-1)
        else:
            print(score_list.index(new_score) + 1)
    else:
        print(-1)
else:
    print(1)