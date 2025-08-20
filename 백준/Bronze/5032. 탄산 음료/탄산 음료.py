e, f, c = map(int, input().split())
tmp, answer = (e + f) // c + (e + f) % c, (e + f) // c

while tmp // c:
    answer += tmp // c
    tmp = tmp // c + tmp % c

print(answer)