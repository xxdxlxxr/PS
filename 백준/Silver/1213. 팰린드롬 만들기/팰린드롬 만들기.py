import collections

name = input()
check_word, mid, result, cnt = collections.Counter(name), '', '', 0

for k, v in list(check_word.items()):
    if v % 2 == 1:
        cnt += 1
        mid = k

        if cnt >= 2:
            print("I'm Sorry Hansoo")
            exit()

for k, v in sorted(check_word.items()):
    result += (k * (v // 2))

print(result + mid + result[::-1])