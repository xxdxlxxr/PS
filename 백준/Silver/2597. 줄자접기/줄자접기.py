r, l = int(input()), 0
point_list = [list(map(float, input().split())) for _ in range(3)]

for i in range(3):
    a, b = point_list[i]

    if a == b:
        continue

    mid = (a + b) / 2
    r, l = mid, min(l, 2 * mid - r)

    for j in range(i + 1, 3):
        for k in range(2):
            if point_list[j][k] > mid:
                point_list[j][k] = 2 * mid - point_list[j][k] 

print('{:.01f}'.format(r - l))