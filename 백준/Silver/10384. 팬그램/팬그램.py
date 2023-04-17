for i in range(int(input())):
    sentence, arr, answer = input().lower(), 26 * [0], 'Not a pangram'

    for unit in sentence:
        if unit.isalpha():
            arr[ord(unit) - 97] += 1

    if min(arr) == 1:
        answer = 'Pangram'
    elif min(arr) == 2:
        answer = 'Double pangram'
    elif min(arr) >= 3:
        answer = 'Triple pangram'

    print('Case {}: {}'.format(i + 1, answer) + min(arr) * '!')