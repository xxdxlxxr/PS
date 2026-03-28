R, C = map(int, input().split())
filter, T, tmp = [list(map(int,input().split())) for r in range(R)], int(input()), []

for r in range(R - 2) :
    for c in range(C - 2) :
        median = []
        
        for i in range(r, r + 3) :
            for j in range(c, c + 3) :
                median.append(filter[i][j])

        median.sort()    
        tmp.append(median[4])

print(sum(num >= T for num in tmp))