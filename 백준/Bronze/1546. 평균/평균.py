N, scores = int(input()), list(map(int, input().split()))

print((sum(scores) * 100 / max(scores)) / N)