n, Fibonacci = int(input()), [0, 1]

for _ in range(n - 1):
    Fibonacci.append(Fibonacci[-2] + Fibonacci[-1])

print(Fibonacci[n])