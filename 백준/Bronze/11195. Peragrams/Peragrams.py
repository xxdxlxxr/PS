from collections import Counter

s_cnt = Counter(input())
print(max(0, sum(1 for v in s_cnt.values() if v % 2 == 1) - 1))