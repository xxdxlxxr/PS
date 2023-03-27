for _ in range(int(input())):
    letter = input()
    sqrtlen_letter = int(len(letter) ** 0.5)
    answer = [0] * sqrtlen_letter ** 2

    for i in range(sqrtlen_letter ** 2):
        answer[sqrtlen_letter * (sqrtlen_letter - (i % sqrtlen_letter) - 1) + i // sqrtlen_letter] = letter[i]

    print(''.join(answer))