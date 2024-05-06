S, loc = input(), 0

while loc < len(S):
    print(S[loc], end='')
    loc += ord(S[loc]) - ord('A') + 1