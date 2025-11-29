S, P = map(int, input().split())
string = input()
cnt_A, cnt_C, cnt_G, cnt_T = map(int, input().split())
i, j, answer = 0, P - 1, 0

d = {'A': 0, 'C': 0, 'G': 0, 'T': 0}

for item in string[i:j]:
    d[item] += 1

while j < S:
    d[string[j]] += 1

    if d['A'] >= cnt_A and d['C'] >= cnt_C and d['G'] >= cnt_G and d['T'] >= cnt_T:
        answer += 1

    d[string[i]] -= 1
    i += 1
    j += 1

print(answer)