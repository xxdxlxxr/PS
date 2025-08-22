N, result = int(input()), []

for _ in range(N):
    ABC = sum(map(int, input().split()))

    if ABC >= 512:
        result.append(ABC)

if result:
    result.sort()
    print(result[0])
else:
    print(-1)