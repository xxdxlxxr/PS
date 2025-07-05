import sys

for A in sys.stdin:
    print('NY'[int(A) % 6 == 0])