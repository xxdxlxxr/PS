self = 'iovwx'
pair = 'bdbpqp'

while 1:
    word = input().rstrip()

    if word == "#":
        break

    answer = []

    for char in word[::-1]:
        if char in self:
            answer.append(char)
        elif char in pair:
            answer.append(pair[pair.index(char) + 1])
        else:
            print("INVALID")
            answer = []
            break
    if answer:
        print(*answer, sep='')