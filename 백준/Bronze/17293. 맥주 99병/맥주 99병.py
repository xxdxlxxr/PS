def bottle(n):
    ret = str(n) if n else 'No more'
    return ret + ' bottle' + (n != 1) * 's'

N = int(input())

for i in range(N, -1, -1):
    print(f'{bottle(i)} of beer on the wall, {bottle(i).lower()} of beer.')
    print(f'Take one down and pass it around, {bottle(i - 1).lower()} of beer on the wall.' if i else f'Go to the store and buy some more, {bottle(N)} of beer on the wall.')
    print()