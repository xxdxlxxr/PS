for _ in range(int(input())):
    word1, word2 = map(sorted, input().split())
    print('Possible' if word1 == word2 else 'Impossible')