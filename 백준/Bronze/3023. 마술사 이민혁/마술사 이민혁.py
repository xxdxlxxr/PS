R, C = map(int, input().split())
card = [list(input()) for _ in range(R)]
card = [[*row, *row[::-1]] for row in [*card, *card[::-1]]]
A, B = map(int, input().split())
A -= 1
B -= 1
card[A][B] = '#.'[card[A][B] == '#']

for row in card:
    print(*row, sep='')