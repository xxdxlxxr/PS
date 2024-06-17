for _ in range(int(input())):
    cnt = dict()

    for char in input():
        if char.isalpha():
            if char not in cnt:
                cnt[char] = 0

            cnt[char] += 1

    values, m = list(cnt.values()), max(cnt.values())

    if values.count(m) == 1:
        for k, v in cnt.items():
            if v == m:
                print(k)
                break
    else:
        print('?')