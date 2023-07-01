def solution(arr):
    cnt = arr.count(2)

    if cnt > 1:
        if arr[-1] == 2:
            return arr[arr.index(2):]
        else:
            return arr[arr.index(2):-arr[::-1].index(2)]
    elif cnt == 1:
        return [2]
    else:
        return [-1]