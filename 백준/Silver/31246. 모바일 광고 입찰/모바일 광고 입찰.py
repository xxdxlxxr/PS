N, K = map(int, input().split())
nums = []

for _ in range(N):
    A, B = map(int, input().split())
    nums.append(B - A)

nums.sort()  # 오름차순 정렬

print(0 if nums[K - 1] < 0 else nums[K - 1])