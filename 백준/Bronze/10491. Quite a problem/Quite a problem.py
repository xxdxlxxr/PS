import sys

for line in sys.stdin:
    if 'problem' in line.rstrip().lower():
        print('yes')
    else:
        print('no')