p, r = map(int, input().split())
print(['weak', 'normal', 'strong', 'very strong'][min(int(5 * p / r), 3)])