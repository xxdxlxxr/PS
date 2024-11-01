final = []

for _ in range(int(input())):
    scores = list(map(int, input().split()))
    final.append(max(scores[:2]) + sum(list(sorted(scores[2:]))[-2:]))

print(max(final))