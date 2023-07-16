arr = [100 * [0] for _ in range(100)]

for _ in range(4):
    Ax, Ay, Bx, By = map(int, input().split())

    for i in range(Ax, Bx):
        for j in range(Ay, By):
            arr[i][j] = 1

print(sum([sum(nums) for nums in arr]))