import sys

for name in sys.stdin.readlines():
    for char in name:
        if char == 'I':
            char = 'E'
        elif char == 'E':
            char = 'I'
        elif char == 'i':
            char = 'e'
        elif char == 'e':
            char = 'i'

        print(char, end='')