w, h = map(int, input().split())
w_list, h_list = [0, w], [0, h]

for _ in range(int(input())):
    wh, n = map(int, input().split())

    if wh:
        w_list.append(n)
    else:
        h_list.append(n)

w_list.sort()
h_list.sort()
answer = 0

for i in range(1, len(w_list)):
    for j in range(1, len(h_list)):
        answer = max(answer, (w_list[i] - w_list[i - 1]) * (h_list[j] - h_list[j - 1]))

print(answer)