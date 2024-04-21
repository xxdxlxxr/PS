for _ in range(int(input())):
    score = sum(char.isalpha() * (ord(char) - ord('A') + 1) for char in input())

    print('PERFECT LIFE' if score == 100 else score)