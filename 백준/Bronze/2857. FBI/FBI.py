answer, flag = [], 0

for i in range(5):
    if 'FBI' in input():
        answer.append(i + 1)

print(' '.join(map(str, answer)) if len(answer) else 'HE GOT AWAY!')