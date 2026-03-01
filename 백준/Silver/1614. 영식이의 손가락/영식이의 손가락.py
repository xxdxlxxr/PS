finger, cnt_number, cnt, answer = int(input()), int(input()), 0, 0

if finger == 1:
    if cnt_number == 0:
        answer += finger - 1
    else:
        answer += 8 * cnt_number
elif finger == 5:
    if cnt_number == 0:
        answer += finger - 1
    else:
        answer += 4 + 8 * cnt_number
else:
    if cnt_number == 0:
        answer += finger - 1
    else:
        answer += 4 * cnt_number + 1
        
        if cnt_number % 2 == 0:
            answer += finger - 2
        else:
            answer += 4 - finger
            
print(answer)