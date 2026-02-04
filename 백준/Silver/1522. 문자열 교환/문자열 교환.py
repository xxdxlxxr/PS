s = input()
cnt = s.count('a')
s, answer = 2 * s, 1000

for i in range(len(s) - cnt):
    answer = min(answer, s[i:i + cnt].count('b'))

print(answer)