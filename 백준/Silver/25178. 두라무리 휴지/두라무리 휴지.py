N, first, second = int(input()), input(), input()

print('YES' if sorted(first) == sorted(second) and first[0] == second[0] and first[-1] == second[-1] and ''.join(char for char in first if char not in ['a', 'e', 'i', 'o', 'u']) == ''.join(char for char in second if char not in ['a', 'e', 'i', 'o', 'u']) else 'NO')