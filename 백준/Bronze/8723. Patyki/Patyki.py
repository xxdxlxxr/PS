abc = sorted(list(map(int, input().split())))

print(2 if len(set(abc)) == 1 else 1 if abc[0] ** 2 + abc[1] ** 2 == abc[2] ** 2 else 0)