D, M = map(int, input().split())
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

print(day[(sum(month[:M]) + D + 2) % 7])