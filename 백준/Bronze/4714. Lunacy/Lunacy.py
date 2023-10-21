while 1:
    X = float(input())

    if X == -1:
        break

    print('Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (X, 0.167 * X))