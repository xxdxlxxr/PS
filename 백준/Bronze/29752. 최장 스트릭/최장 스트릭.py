N, s, arr, cnt = int(input()), list(map(int, input().split())), [], 0

for number in s:
    if not number:
        arr.append(cnt)
        cnt = 0
    else:
        cnt += 1

arr.append(cnt)
print(max(arr))