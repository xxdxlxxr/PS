import sys

dic, total = dict(), 0

while 1:
    word = sys.stdin.readline().rstrip()

    if word == '':
        break

    total += 1

    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

tmp = dict(sorted(dic.items()))

for i in tmp:
    per = 100 * tmp[i] / total
    print("%s %.4f" % (i, per))