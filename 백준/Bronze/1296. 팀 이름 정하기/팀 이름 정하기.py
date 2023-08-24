name, arr = input(), []

for _ in range(int(input())):
    team_name, total = input(), 1
    love_count = [(name + team_name).count(char) for char in 'LOVE']

    for i in range(3):
        for j in range(i + 1, 4):
            total *= love_count[i] + love_count[j]

    arr.append([100 - total % 100, team_name])

print(sorted(arr)[0][1])