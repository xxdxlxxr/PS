word = input().upper()
word_trans = list(set(word))
cnt = [word.count(alpha) for alpha in word_trans]

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(word_trans[(cnt.index(max(cnt)))])