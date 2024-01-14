N, file, cluster = int(input()), list(map(int, input().split())), int(input())

print(sum(0 if not size else size // cluster + (size % cluster != 0) for size in file) * cluster)