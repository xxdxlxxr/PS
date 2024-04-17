for _ in range(int(input())):
    M, CN = input().split()
    print(*(ord(char) - ord('A') + 1 for char in input().split()) if CN == 'C' else (chr(num + ord('A') - 1) for num in map(int, input().split())))