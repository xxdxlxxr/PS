def check_valid(now, loc):
    if abs(ord(now[0]) - ord(loc[0])) == 2 and abs(int(now[1]) - int(loc[1])) == 1:
        return 1
    elif abs(ord(now[0]) - ord(loc[0])) == 1 and abs(int(now[1]) - int(loc[1])) == 2:
        return 1
    
    return 0

now, tmp, cnt = input(), [], 1
tmp.append(now)

for i in range(35):
    loc = input()
    tmp.append(loc)

    if check_valid(now, loc) == 1:
        cnt += 1
        now = loc
    else:
        break

print('Valid' if cnt == 36 and len(set(tmp)) == 36 and check_valid(tmp[0], tmp[-1]) else 'Invalid')