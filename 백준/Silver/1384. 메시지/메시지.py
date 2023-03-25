cnt = 1

while 1:
    n, papers, answer = int(input()), [], []

    if not n:
        break

    for i in range(n):
        paper = list(input().split())
        papers.append(paper)

        for j in range(1, n):
            if paper[j] == 'N':
                answer.append([i, j])

    print('Group {}'.format(cnt))

    if answer:
        for unit in answer:
            print('{} was nasty about {}'.format(papers[unit[0] - unit[1]][0], papers[unit[0]][0]))
    else:
        print('Nobody was nasty')

    print()

    cnt += 1