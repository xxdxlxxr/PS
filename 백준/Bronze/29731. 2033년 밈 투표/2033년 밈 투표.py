pledge = ['give you up', 'let you down', 'run around and desert you', 'make you cry', 'say goodbye', 'tell a lie and hurt you', 'stop']

for _ in range(int(input())):
    S = input().split()

    if len(S) < 3 or S[:2] != ['Never', 'gonna'] or ' '.join(S[2:]) not in pledge:
        print('Yes')
        break
else:
    print('No')