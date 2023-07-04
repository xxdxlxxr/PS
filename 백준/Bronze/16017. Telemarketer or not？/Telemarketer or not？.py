numbers = [int(input()) for _ in range(4)]

print('ignore' if numbers[0] > 7 and numbers[3] > 7 and numbers[1] == numbers[2] else 'answer')