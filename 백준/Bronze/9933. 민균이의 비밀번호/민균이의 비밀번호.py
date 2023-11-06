txt = [input() for _ in range(int(input()))]

for word in txt:
    if ''.join(reversed(word)) in txt:
        break

print(len(word), word[len(word) // 2])