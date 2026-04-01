tmp_1, tmp_2, flag = 0, 0, 0

for i in range(int(input())):
    team, time = input().split()
    m, s = map(int, time.split(':'))
    
    if team == '1':
        if flag == 0:
            tmp_1 += 48 * 60 - (60 * m + s)
        
        flag += 1
        
        if flag == 0:
            if tmp_2 > 0:
                tmp_2 -= 48 * 60 - (60 * m + s)
    else:
        if flag == 0:
            tmp_2 += 48 * 60 - (60 * m + s)
        
        flag -= 1

        if flag == 0:
            if tmp_1 > 0:
                tmp_1 -= 48 * 60 - (60 * m + s)

        
print('{:0>2}:{:0>2}'.format(tmp_1 // 60, tmp_1 % 60))
print('{:0>2}:{:0>2}'.format(tmp_2 // 60, tmp_2 % 60))