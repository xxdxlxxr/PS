N, candy, tmp = int(input()), [], 0

for i in range(N):
    candy.append(int(input()))  
    tmp += (-1) ** i * candy[i]

a = tmp // 2
print(a)

for i in range(N - 1):
    a = candy[i] - a
    print(a)