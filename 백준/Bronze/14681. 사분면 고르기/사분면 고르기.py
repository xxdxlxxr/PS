x = int(input())
y = int(input())
arr = [[3, 2],
       [4, 1]]

print(arr[(x // abs(x) + 1) // 2][(y // abs(y) + 1) // 2])