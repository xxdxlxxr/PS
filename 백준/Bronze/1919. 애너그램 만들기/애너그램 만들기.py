a, b = 26 * [0], 26 * [0]

for i in input():
    a[ord(i) - ord('a')] += 1

for i in input():
    b[ord(i) - ord('a')] += 1

print(sum(abs(a[i] - b[i]) for i in range(26)))