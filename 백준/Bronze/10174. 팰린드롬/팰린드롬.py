for _ in range(int(input())):
    string, answer = input(), 1

    for i in range(len(string) // 2):
        if string[i].lower() != string[-(i + 1)].lower():
            answer = 0
            break

    print('Yes' if answer else 'No')