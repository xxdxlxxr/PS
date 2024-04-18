day = [int(input()) for _ in range(2)]

print('Special' if day == [2, 18] else 'Before' if day < [2, 18] else 'After')