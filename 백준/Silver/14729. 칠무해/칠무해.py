scores = sorted(float(input()) for _ in range(int(input())))

for i in range(7):
    print('%.3f' % scores[i])