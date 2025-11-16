N, S = map(int, input().split())
nums, cnt = list(map(int, input().split())), 0

def func(i, tmp):
    global cnt

    if i >= N:
        return

    tmp += nums[i]

    if tmp == S:
        cnt += 1

    func(i + 1, tmp)
    func(i + 1, tmp - nums[i])

func(0, 0)
print(cnt)