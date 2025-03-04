while 1:
    name, age, weight = input().split()

    if name == '#':
        break

    print(name, 'Senior' if int(age) > 17 or int(weight) >= 80 else 'Junior')