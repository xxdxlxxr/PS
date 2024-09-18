for i, num in enumerate(reversed(bin(int(input()))[2:])):
    if num == '1':
        print(i, end=' ')