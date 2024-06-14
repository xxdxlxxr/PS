n = int(input())
print('Happy' if 2 * sum(num % 2 == 0 for num in map(int, input().split())) > n else 'Sad')