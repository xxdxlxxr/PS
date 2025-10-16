N, A, B = map(int, input().split())
print('Anything' if A == B else 'Bus' if A < B else 'Subway')