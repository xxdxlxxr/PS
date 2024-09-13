S, K, H = map(int, input().split())
print('OK' if S + K + H >= 100 else ['Soongsil', 'Korea', 'Hanyang'][(S, K, H).index(min(S, K, H))])