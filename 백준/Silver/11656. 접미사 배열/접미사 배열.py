S = input()

for string in sorted(S[i:] for i in range(len(S))):
    print(string)