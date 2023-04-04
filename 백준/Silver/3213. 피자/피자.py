arr = 3 * [0]

for _ in range(int(input())):
    amount = input()

    if amount[-1] == '2':
        arr[1] += 1
    else:
        arr[int(amount[0]) - 1] += 1

answer = arr[1] // 2
arr[1] %= 2

temp = min(arr[0], arr[2])
arr[0] -= temp
arr[2] -= temp
answer += temp

temp = min(arr[0], arr[1])
arr[0] -= temp
arr[1] -= temp
answer += temp

temp = arr[0] // 4
answer += temp
arr[0] -= temp

if arr[0]:
    answer += 1

answer += arr[1] + arr[2]

print(answer)