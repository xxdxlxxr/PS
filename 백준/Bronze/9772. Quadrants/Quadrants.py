x, y = 1, 1
quadrant = [['Q3', 'Q2'],
            ['Q4', 'Q1']]

while x or y:
    x, y = map(float, input().split())

    if x and y:
        print(quadrant[int(x / abs(x) / 2 + .5)][int(y / abs(y) / 2 + .5)])
    else:
        print('AXIS')