N = int(input())
arr = 9 * [0]

for num in str(N):
    if int(num) == 6 or int(num) == 9:
        arr[6] += 1
    else:
        arr[int(num)] += 1

arr[6] = (arr[6] + 1) // 2

print(max(arr))