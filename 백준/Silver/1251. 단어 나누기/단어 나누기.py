word, tmp, answer = list(input()), [], []

for i in range(1, len(word) - 1):
    for j in range(i + 1, len(word)):
        a = word[:i]
        b = word[i:j]
        c = word[j:]
        a.reverse()
        b.reverse()
        c.reverse()
        tmp.append(''.join(a + b + c))

print(sorted(tmp)[0])