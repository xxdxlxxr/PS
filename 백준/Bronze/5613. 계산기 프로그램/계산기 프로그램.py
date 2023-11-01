answer = input()

while 1:
    a = input()

    if a == '=':
        break

    b = input()
    answer = str(int(eval(answer + a + b)))

print(answer)