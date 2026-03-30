for _ in range(int(input())):
    B, D = input().split()
    print(sum(map(int, list(D))) % (int(B) - 1))