arr = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]
A, B, answer = input(), input(), []

for i in range(len(A)):
    answer.append(arr[ord(A[i]) - 65])
    answer.append(arr[ord(B[i]) - 65])

while len(answer) != 2:
    temp = []

    for i in range(1, len(answer)):
        temp.append((answer[i] + answer[i - 1]) % 10)

    answer = temp

print("{}{}".format(answer[0], answer[1]))