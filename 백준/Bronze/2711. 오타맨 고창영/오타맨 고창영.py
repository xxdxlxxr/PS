for _ in range(int(input())):
    i, string = input().split()
    i = int(i)
    print(string[:i - 1] + string[i:])