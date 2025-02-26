form = input()
print(['NO', 'YES'][eval(form[:5]) == int(form[-1])])