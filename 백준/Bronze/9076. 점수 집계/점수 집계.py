for _ in range(int(input())):
    scores = sorted(map(int, input().split()))
    print(sum(scores[1:4]) if scores[3] - scores[1] < 4 else 'KIN')