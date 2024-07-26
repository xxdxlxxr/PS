N, answer = int(input()), [1]

if N - 1:
    cards = [i for i in range(2, N + 1)]

    while len(cards) - 1:
        cards.append(cards.pop(0))
        answer.append(cards.pop(0))
    print(*answer + cards)
else:
    print(*answer)