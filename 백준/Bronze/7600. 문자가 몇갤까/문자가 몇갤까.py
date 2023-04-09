while 1:
    sentence, answer = input(), []

    if sentence == '#':
        break

    for unit in sentence.lower():
        if unit.isalpha():
            answer.append(unit)

    print(len(set(answer)))