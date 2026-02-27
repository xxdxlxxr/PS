N, L  = map(int,input().split())
nums, answer = sorted(list(map(int,input().split()))), 1
start = nums[0] - 1
end = start + L

for i in range(1, N):
    if nums[i] <= end:
        continue
    else:
        answer += 1
        start = nums[i] - 1
        end = start + L
        
print(answer)