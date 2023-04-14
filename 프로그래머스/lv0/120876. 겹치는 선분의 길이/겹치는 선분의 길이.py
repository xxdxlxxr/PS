def solution(lines):
    store, answer = [], []

    for line in lines:
        for i in range(line[0], line[1]):
            if i in store:
                answer.append(i)
            else:
                store.append(i)

    return len(set(answer))