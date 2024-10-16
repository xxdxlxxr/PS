input()
index, m = -1, 0

for i in range(9):
    tmp = max(map(int, input().split()))

    if tmp > m:
        index = i
        m = tmp

print(['PROBRAIN', 'GROW', 'ARGOS', 'ADMIN', 'ANT', 'MOTION', 'SPG', 'COMON', 'ALMIGHTY'][index])