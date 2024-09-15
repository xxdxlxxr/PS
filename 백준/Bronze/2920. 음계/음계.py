numbers = list(map(int, input().split()))
print('ascending' if numbers == list(range(1, 9)) else 'descending' if numbers == list(range(8, 0, -1)) else 'mixed')