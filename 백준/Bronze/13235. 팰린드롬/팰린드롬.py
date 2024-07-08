word = input()
print('true' if word == ''.join(reversed(word)) else 'false')