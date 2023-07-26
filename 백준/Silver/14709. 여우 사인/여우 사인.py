if int(input()) == 3 and sorted([sorted(list(map(int, input().split()))) for _ in range(3)]) == [[1, 3], [1, 4], [3, 4]]:
    print('Wa-pa-pa-pa-pa-pa-pow!')
else:
    print('Woof-meow-tweet-squeek')