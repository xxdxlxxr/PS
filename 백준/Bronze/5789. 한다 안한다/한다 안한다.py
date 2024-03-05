for _ in range(int(input())):
    numbers = input()
    print('Do-it' + (numbers[len(numbers) // 2 - 1] != numbers[len(numbers) // 2]) * '-Not')