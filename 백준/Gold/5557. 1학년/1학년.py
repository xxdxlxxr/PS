N, nums = int(input()), list(map(int, input().split()))
answer = [21 * [0] for _ in range(N - 1)]
answer[0][nums[0]] += 1

for i in range(1, N - 1):
    for j in range(21):
        if answer[i - 1][j]:
            if j - nums[i] >= 0: answer[i][j - nums[i]] += answer[i - 1][j]
            if j + nums[i] <= 20: answer[i][j + nums[i]] += answer[i - 1][j]
            
print(answer[-1][nums[-1]])