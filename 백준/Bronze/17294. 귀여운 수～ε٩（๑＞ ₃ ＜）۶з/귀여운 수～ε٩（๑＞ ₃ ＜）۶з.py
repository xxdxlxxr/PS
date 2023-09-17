k = list(map(int, input()))
answer = 1

if len(k) != 1:
    diff = k[1] - k[0]

    for i in range(2, len(k)):
        if k[i] - k[i - 1] != diff:
            answer = not(answer)
            break

print('◝(⑅•ᴗ•⑅)◜..°♡ 뀌요미!!' if answer else '흥칫뿡!! <(￣ ﹌ ￣)>')