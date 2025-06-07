for _ in range(int(input())):
    A, B = input().split()
    print(f'{A} & {B} are' + (sorted(A) != sorted(B)) * ' NOT' + ' anagrams.')