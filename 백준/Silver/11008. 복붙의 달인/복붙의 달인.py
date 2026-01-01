for _ in range(int(input())):
    s, p = input().split()
    print(len(s.replace(p, "@")))