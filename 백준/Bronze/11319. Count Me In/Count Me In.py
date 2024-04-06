for _ in range(int(input())):
    sentence, consonants, vowels = input(), 0, 0

    for alpha in sentence:
        if alpha.isalpha():
            if alpha in 'AEIOUaeiou':
                consonants += 1
            else:
                vowels += 1

    print(vowels, consonants)