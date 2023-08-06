def solution(arr):
    return arr if len(arr) == 1 else arr + (2 ** (len(bin(len(arr) - 1)) - 2) - len(arr)) * [0]