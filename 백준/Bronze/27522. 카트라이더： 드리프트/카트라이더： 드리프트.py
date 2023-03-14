records, sum = [], 0
score = [10, 8, 6, 5, 4, 3, 2, 1, 0]

for _ in range(8):
    records.append(input())

records.sort()

for i in range(8):
    if records[i][-1] == 'R':
        sum += score[i]
    else:
        sum -= score[i]

print('Red') if sum > 0 else print('Blue')