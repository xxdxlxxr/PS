answer = -1

for i in range(9):
    nums = list(map(int, input().split()))

    for j in range(9):
        if nums[j] > answer:
            answer, row, col = nums[j], i, j

print(answer)
print(row + 1, col + 1)