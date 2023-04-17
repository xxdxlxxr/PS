def solution(n, words):
    store = [words[0]]

    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0] or words[i + 1] in store:
            return [(i + 1) % n + 1, (i + 1) // n + 1]
        else:
            store.append(words[i + 1])

    return [0, 0]