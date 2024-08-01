def gcd(a, b):
    while b:
        a, b = b, a % b

    return a

n, m = map(int, input().split(':'))
GCD = gcd(n, m)
print(f'{n // GCD}:{m // GCD}')