for _ in range(int(input())):
    r, e, c = map(int, input().split())
    rc = r + c
    print('does not matter' if rc == e else 'do not advertise' if rc > e else 'advertise')