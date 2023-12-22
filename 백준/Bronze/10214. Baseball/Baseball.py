for _ in range(int(input())):
    scores = [0, 0]

    for _ in range(9):
        Y, K = map(int, input().split())
        scores[0] += Y
        scores[1] += K

    print('Draw' if scores[0] == scores[1] else 'Yonsei' if scores[0] > scores[1] else 'Korea')