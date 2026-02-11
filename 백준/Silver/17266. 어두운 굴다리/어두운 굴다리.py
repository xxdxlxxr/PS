def function(location, height):
    if height < location[0]:
        return 0
    
    for i in range(1, M):
        if location[i] > 2 * height + location[i - 1]:
            return 0
        
    if N > height + location[-1]:
        return 0
    
    return 1

N, M = int(input()), int(input())
x = list(map(int, input().split()))
start, end, answer = 1, N, N

while start <= end:
    mid = (start + end) // 2

    if function(x, mid):
        answer = mid
        end = mid - 1
    else:
        start = mid + 1

print(answer)