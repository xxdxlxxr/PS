word, integer_set, tmp = input(), set(), ''

for i, char in enumerate(word):
    if char.isdigit():
        tmp += char
    elif char.isalpha() and len(tmp) != 0:
        integer_set.add(tmp)
        tmp = ''
    elif char.isalpha():
        tmp = ''

    if i + 1 == len(word) and len(tmp) != 0:
        integer_set.add(tmp)

print(len(integer_set))