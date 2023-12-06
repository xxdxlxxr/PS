N = int(input())
print(sum(ord(char) - ord('A') for char in input()) + N)