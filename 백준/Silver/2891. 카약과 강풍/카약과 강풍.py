N, S, R = map(int, input().split())
team_1, team_2 = set(map(int, input().split())), set(map(int, input().split()))
intersection = team_1 & team_2
team_1, team_2, answer = list(team_1 - intersection), list(team_2 - intersection), 0

if not team_1:
    answer = 0
else:
    for t in sorted(team_1):
        if t - 1 in team_2:
            team_2.remove(t - 1)
        elif t + 1 in team_2:
            team_2.remove(t + 1)
        else:
            answer += 1  
                
print(answer)