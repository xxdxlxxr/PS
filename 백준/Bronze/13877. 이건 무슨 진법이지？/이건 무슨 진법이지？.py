for _ in range(int(input())):
    K, num = input().split()

    print(int(K), int(num, 8) if max(num) < '8' else 0, int(num), int(num, 16))