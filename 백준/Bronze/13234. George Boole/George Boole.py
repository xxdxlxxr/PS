words = input().split()
words[0], words[2] = words[0] == 'true', words[2] == 'true'

if words[1] == 'AND':
    print(str(words[0] and words[2]).lower())
else:
    print(str(words[0] or words[2]).lower())