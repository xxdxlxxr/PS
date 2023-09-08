arr = 10 * [0]

for _ in range(5):
    number = int(input())
    arr[number] = int(not(arr[number]))

print(arr.index(1))