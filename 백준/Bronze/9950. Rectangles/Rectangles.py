while 1:
    l, w, a = map(int, input().split())

    if l + w + a == 0:
        break

    if not l:
        print(a // w, w, a)
    elif not w:
        print(l, a // l, a)
    else:
        print(l, w, l * w)