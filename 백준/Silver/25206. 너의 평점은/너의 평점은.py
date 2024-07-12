grade, total, score = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}, 0, 0

for _ in range(20):
    tmp = input().split()

    if tmp[2] in 'P':
        continue

    total += float(tmp[1])
    score += float(tmp[1]) * grade[tmp[2]]

print(f'{score / total:.6f}' if total else f'{0:.6f}')