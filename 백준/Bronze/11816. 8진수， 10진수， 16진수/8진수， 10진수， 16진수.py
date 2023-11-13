X = input()

print(int(X, 16) if X[:2] == '0x' else int(X, 8) if X[0] == '0' else X)