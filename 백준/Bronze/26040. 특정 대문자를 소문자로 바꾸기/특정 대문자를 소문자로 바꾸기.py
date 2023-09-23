A, B = input(), input().split()

print(''.join(chr(ord(char) + 32) if char in B else char for char in A))