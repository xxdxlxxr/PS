N, answer = input(), 0

for i, num in enumerate(N):
    answer += 2 * ((i >= len(N) >> 1) - .5) * int(num)

print('READY' if answer else 'LUCKY')