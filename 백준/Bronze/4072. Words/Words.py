while 1:
    s = input()

    if s == '#':
        break

    print(*(''.join(reversed(word)) for word in s.split()))