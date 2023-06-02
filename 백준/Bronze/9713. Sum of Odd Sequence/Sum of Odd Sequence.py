for _ in range(int(input())):
    print(sum([i + 1 for i in range(int(input())) if not(i % 2)]))