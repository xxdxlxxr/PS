import sys

cnt = 26 * [0]

for line in sys.stdin.readlines():
    for char in line:
        if char.isalpha():
            cnt[ord(char) - ord('a')] += 1

m = max(cnt)

for i in range(26):
    if cnt[i] == m:
        print(chr(i + ord('a')), end='')