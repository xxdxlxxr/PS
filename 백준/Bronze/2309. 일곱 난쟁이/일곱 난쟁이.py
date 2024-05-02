heights = sorted(int(input()) for _ in range(9))
tmp, check = sum(heights) - 100, 0

for i in range(8):
    for j in range(i, 9):
        if heights[i] + heights[j] == tmp:
            check = 1
            break

    if check:
        break

for k in range(9):
    if k != i and k != j:
        print(heights[k])