N, cnt, answer = input(), 4 * [0], 0

for num in N:
    if num in '2018':
        cnt['2018'.index(num)] += 1
    else:
        answer = 1
        break

if answer:
    print(0)
else:
    print(8 if sum(cnt) == len(N) and min(cnt) == max(cnt) else 2 if min(cnt) != 0 else 1 if sum(cnt) == len(N) else 0)