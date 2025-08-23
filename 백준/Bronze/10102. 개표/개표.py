input()
tmp = sum(2 * (v == 'A') - 1 for v in input())
print('Tie' if tmp == 0 else 'A' if tmp > 0 else 'B')