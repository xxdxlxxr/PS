N = int(input())
i, cnt, arr = 1, N, ''

while 1:
    if cnt - 9 * i * 10 ** (i - 1) >= 0:
        cnt -= 9 * i * 10 ** (i - 1)
        i += 1
    else:
        break

print(str(10 ** (i - 1) + (cnt - 1) // i)[(cnt - 1) % i])