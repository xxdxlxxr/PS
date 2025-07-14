try:
    while True :
        a, b = map(int, input().split())
        print(b // (a + 1))
except:
    exit(0)