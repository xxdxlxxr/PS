scores = [sum(map(int, input().split())) for _ in range(5)]
print(scores.index(max(scores)) + 1, max(scores))