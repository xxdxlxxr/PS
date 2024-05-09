input()
seat, answer = 101 * [0], 0

for num in map(int, input().split()):
    if seat[num]:
        answer += 1

    seat[num] = 1

print(answer)