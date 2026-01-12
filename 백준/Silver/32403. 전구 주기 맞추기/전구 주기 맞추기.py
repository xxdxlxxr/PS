N, T = map(int, input().split())
A, answer = list(map(int, input().split())), 0

for a in A:
    num = 0

    while 1:
        if T % (a + num)  == 0:
            break
        elif T % (a - num) == 0:
            break
        else:
            num += 1

    answer += num
    
print(answer)