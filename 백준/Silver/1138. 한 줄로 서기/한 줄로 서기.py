N, nums = int(input()), list(map(int, input().split()))
answer = N * [0]

for i in range(N):
    cnt = 0

    for j in range(N):
        if cnt == nums[i] and answer[j] == 0:
            answer[j] = i + 1
            break
        elif answer[j] == 0:
            cnt += 1

print(*answer)