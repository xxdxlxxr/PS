N, C = map(int, input().split())
nums, dic = list(map(int, input().split())), {}

for i in range(len(nums)):
    if nums[i] not in dic:
        dic[nums[i]] = [i, 1, nums[i]]
    else:
        dic[nums[i]][1] += 1

print(*(i[2] for i in sorted(dic.values(), key=lambda x :(-x[1], x[0])) for j in range(i[1])))