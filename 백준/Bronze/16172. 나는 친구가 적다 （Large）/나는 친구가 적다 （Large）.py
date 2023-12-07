S = ''.join([char.isalpha() * char for char in input()])

print(1 if input() in S else 0)