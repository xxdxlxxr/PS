N, A, B = map(int, input().split())
S = input()

print(S[:A - 1] + ''.join(list(reversed(S[A - 1:B]))) + S[B:])