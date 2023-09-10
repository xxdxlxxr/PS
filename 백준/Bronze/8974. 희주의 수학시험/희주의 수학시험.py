A, B = map(int, input().split())
arr = [0]

for i in range(46):
    arr += i * [i]

print(sum(arr[A:B + 1]))