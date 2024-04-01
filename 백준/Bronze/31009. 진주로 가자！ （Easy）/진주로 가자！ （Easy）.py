dic = dict()

for _ in range(int(input())):
    D, C = input().split()
    dic[D] = int(C)

print(dic['jinju'])
print(sum(value > dic['jinju'] for value in dic.values()))