for i in range(1, int(input()) + 1):
    N = int(input())
    print(f'Case #{i}: {'Round 1' if N > 4500 else 'Round 2' if N > 1000 else 'Round 3' if N > 25 else 'World Finals'}')