input()
move = sum(map(int, input().split()))
print('Right' if move > 0 else 'Left' if move < 0 else 'Stay')