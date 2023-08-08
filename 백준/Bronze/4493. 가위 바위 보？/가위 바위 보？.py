result = [0, -1, 1]

for _ in range(int(input())):
    score = 0

    for _ in range(int(input())):
        P1, P2 = input().split()
        score += result['RSP'.index(P1) - 'RSP'.index(P2)]

    print(f'Player {(score < 0) + 1}' if score else 'TIE')