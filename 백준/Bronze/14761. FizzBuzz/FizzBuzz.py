X, Y, N = map(int, input().split())

for i in range(1, N + 1):
    print('FizzBuzz' if i % X == 0 and i % Y == 0 else 'Fizz' if i % X == 0 else 'Buzz' if i % Y == 0 else i)