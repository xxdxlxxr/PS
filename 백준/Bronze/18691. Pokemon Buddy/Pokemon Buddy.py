for _ in range(int(input())):
    G, C, E = map(int, input().split())
    print(max((2 * G - 1) * (E - C), 0))