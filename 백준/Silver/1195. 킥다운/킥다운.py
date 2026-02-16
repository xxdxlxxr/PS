gear_A, gear_B = input(), input()
tmp = len(gear_A) + len(gear_B)
ai, aj, bi, bj, answer = len(gear_A) - 1, len(gear_A) - 1, 0, 0, tmp

while 1:
    for i in range(aj - ai + 1):
        if gear_A[ai + i] == gear_B[bi + i] and gear_B[bi + i] == '2':
            break
    else:
        answer = min(answer, tmp - aj + ai - 1)
    
    ai -= 1

    if ai == -1:
        ai = 0
        bi += 1
    
    bj += 1

    if bj == len(gear_B):
        bj = len(gear_B) - 1
        aj -= 1

    if ai > aj or bi > bj:
        break

print(answer)