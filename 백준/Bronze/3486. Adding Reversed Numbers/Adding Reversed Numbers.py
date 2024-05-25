for _ in range(int(input())):
    print(int(''.join(reversed(str(sum(map(int, ''.join(list(reversed(input()))).split())))))))