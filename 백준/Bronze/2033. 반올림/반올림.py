N, digit = int(input()), 10

while N > digit:
    N = (N // digit + (N % digit // (digit // 10) > 4)) * digit
    digit *= 10

print(N)