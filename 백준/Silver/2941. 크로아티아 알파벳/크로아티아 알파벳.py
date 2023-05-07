s = input()

for unit in ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']:
    s = s.replace(unit, 'a')

print(len(s))