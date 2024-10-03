tmp = float(input())

while 1:
    temp = float(input())

    if temp == 999:
        break

    print('%.2f' % (temp - tmp))
    tmp = temp