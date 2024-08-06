_, tmp = int(input()), []

for topping in input().split():
    if topping not in tmp and topping[-6:] == 'Cheese':
        tmp.append(topping)

    if len(tmp) == 4:
        print('yummy')
        break
else:
    print('sad')