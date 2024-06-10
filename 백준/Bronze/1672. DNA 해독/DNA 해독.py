N, string = int(input()), list(input())
table = {"AA": "A", "AG": "C", "AC": "A", "AT": "G",
         "GA": "C", "GG": "G", "GC": "T", "GT": "A",
         "CA": "A", "CG": "T", "CC": "C", "CT": "G",
         "TA": "G", "TG": "A", "TC": "G", "TT": "T"}

for _ in range(N - 1):
    tmp = string[-2] + string[-1]
    del string[-2:]
    string.append(table[tmp])

print(*string)