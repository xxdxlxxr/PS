for char in input():
    print(sum(map(int, str(ord(char)))) * char)