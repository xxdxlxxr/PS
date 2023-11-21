S1, S2 = map(int, input().split())
correct = 1

for i in range(S1 + S2):
    A, B = map(int, input().split())

    if A != B:
        correct = 0
        break

print('Accepted' if i + 1 == S1 + S2 and correct else 'Wrong Answer' if i < S1 else 'Why Wrong!!!')