n, nums, k = int(input()), list(map(int, input().split())), int(input())
left, right, total, answer = 0, 0, 0, 0

while left <= right:
    if total > k:
        answer += n - right + 1
        total -= nums[left]
        left += 1
    elif right == n:
        break
    else:
        total += nums[right]
        right += 1

print(answer)