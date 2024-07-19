doc, word, cnt = input(), input(), 0

while doc.find(word) + 1:
    cnt += 1
    doc = doc[doc.find(word) + len(word):]

print(cnt)