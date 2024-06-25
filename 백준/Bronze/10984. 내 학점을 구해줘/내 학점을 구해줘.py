for _ in range(int(input())):
    answer = [0, 0]

    for _ in range(int(input())):
        C, G = input().split()
        C, G = int(C), float(G)
        answer[0] += C
        answer[1] += C * G

    answer[1] /= answer[0]
    print(f'{answer[0]} {answer[1]:.1f}')