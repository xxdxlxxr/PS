M, N = map(int, input().split())
dic = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
       '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
tmp = [[i, ' '.join([dic[j] for j in str(i)])] for i in range(M, N + 1)]
tmp.sort(key=lambda x: x[1])

for i in range(len(tmp)):
    if i % 10 == 0 and i != 0:
        print(sep="\n")

    print(tmp[i][0], end=' ')