L, user_input, M, r, answer = int(input()), input(), 1234567891, 31, 0

for i in range(len(user_input)):
    num = ord(user_input[i]) - 96
    answer += num * (r ** i)

print(answer % M)