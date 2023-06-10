print('Gnomes:')

for _ in range(int(input())):
    A, B, C = map(int, input().split())

    print('Ordered' if A > B > C or A < B < C else 'Unordered')