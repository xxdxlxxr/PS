R, C = map(int, input().split())
card = []

for _ in range(R):
    design = input()
    card.append(list(design) + list(reversed(design)))

A, B = map(int, input().split())

for i in range(2 * R):
    for j in range(2 * C):
        char = card[min(i, 2 * R - i - 1)][j]

        if i + 1 == A and j + 1 == B:
            print('#.'[char == '#'], end='')
        else:
            print(char, end='')

    print()