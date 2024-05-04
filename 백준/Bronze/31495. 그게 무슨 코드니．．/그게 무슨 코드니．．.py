S = input()
print('CE' if S[0] != '"' or S[-1] != '"' or len(S) < 3 else S[1:-1])