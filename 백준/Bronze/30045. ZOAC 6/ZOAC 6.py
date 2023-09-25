answer = 0

for _ in range(int(input())):
    S = input()
    answer += '01' in S or 'OI' in S

print(answer)