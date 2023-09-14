for i in range(int(input())):
    ABC = list(map(int, input().split()))
    answer = 'invalid!' if max(ABC) >= sum(ABC) - max(ABC) else 'equilateral' if len(set(ABC)) == 1 else 'isosceles' if len(set(ABC)) == 2 else 'scalene'

    print(f'Case #{i + 1}: {answer}')