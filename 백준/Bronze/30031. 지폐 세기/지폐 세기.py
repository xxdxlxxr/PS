arr = [1000, 5000, 10000, 50000]

print(sum(arr[(list(map(int, input().split()))[0] - 136) // 6] for _ in range(int(input()))))