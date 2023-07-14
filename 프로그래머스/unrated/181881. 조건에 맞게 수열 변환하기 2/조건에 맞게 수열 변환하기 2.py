def solution(arr):
    check, answer = 1, 0

    while check:
        tmp, arr = arr, [arr[i] // ((arr[i] >= 50 and not (arr[i] % 2)) + 1) * ((arr[i] < 50 and arr[i] % 2) + 1) + (arr[i] < 50 and arr[i] % 2) for i in range(len(arr))]

        if tmp == arr:
            check = 0
        else:
            answer += 1

    return answer