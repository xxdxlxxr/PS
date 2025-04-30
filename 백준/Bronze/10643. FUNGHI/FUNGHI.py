S, cnt = [int(input()) for _ in range(8)], []
length = len(S)
print(max(sum(S[i:i + 4]) if i + 4 < length else sum(S[i:] + S[:i + 4 - length]) for i in range(8)))