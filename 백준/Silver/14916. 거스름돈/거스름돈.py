n, five, answer = int(input()), 0, []

while n >= 0:
    if not(n % 2):
        answer.append([five, n // 2])

    five += 1
    n -= 5

if answer:
    print(sum(answer[-1]))
else:
    print(-1)