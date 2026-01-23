N = input()
print(sum(9 * 10 ** (i - 1) * i for i in range(1, len(N))) + (int(N) - 10 ** (len(N) - 1) + 1) * len(N))