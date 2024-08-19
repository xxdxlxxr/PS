scores = sorted([[int(input()), i + 1] for i in range(8)], reverse=True)[:5]
print(sum(score for score, _ in scores))
print(*sorted(rank for _, rank in sorted(scores)))