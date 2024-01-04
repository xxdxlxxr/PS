N = int(input())

print(sum(min(num, N) for num in map(int, input().split())))