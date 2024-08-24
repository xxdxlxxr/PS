for i in range(3):
    string = input()

    if string.isnumeric():
        answer = int(string) - i + 3
        break

print('FizzBuzz' if answer % 15 == 0 else 'Fizz' if answer % 3 == 0 else 'Buzz' if answer % 5 == 0 else answer)