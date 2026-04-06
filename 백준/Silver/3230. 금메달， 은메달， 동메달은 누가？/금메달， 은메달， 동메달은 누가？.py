N, M = map(int, input().split())
first_rank, current_rankings, answer = (N + 1) * [0], [], []

for player in range(1, N + 1):
    current_rankings.insert(int(input()) - 1, player)

for i, player in enumerate(current_rankings):
    first_rank[player] = i + 1

for player in list(reversed(current_rankings[:M])):
    answer.insert(int(input()) - 1, player)

print(answer[0])
print(answer[1])
print(answer[2])