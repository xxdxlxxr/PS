N, S = int(input()), input()

print(sum((S[i] == 'O') * (i + 1) for i in range(N)) + sum((len(str) - 1) * len(str) // 2 for str in S.split('X')))