score = 0

for i in range(3): score += (3 - i) * int(input())
for i in range(3): score -= (3 - i) * int(input())

print('A' if score > 0 else 'B' if score < 0 else 'T')