names = []

for _ in range(int(input())):
    names.append(input())

if names == sorted(names):
    print('INCREASING')
elif names == sorted(names, reverse = True):
    print('DECREASING')
else:
    print('NEITHER')