answer = 0

for _ in range(int(input())):
    if input() == 'anj':
        answer = 1
        break

print('뭐야;' if answer else '뭐야?')