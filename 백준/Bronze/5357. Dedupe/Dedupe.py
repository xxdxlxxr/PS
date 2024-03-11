for _ in range(int(input())):
    string = input()
    answer = string[0]

    for char in string[1:]:
        if char != answer[-1]:
            answer += char

    print(answer)