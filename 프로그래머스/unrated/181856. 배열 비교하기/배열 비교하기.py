def solution(arr1, arr2):
    return (sum(arr1) != sum(arr2)) * (2 * (sum(arr1) > sum(arr2)) - 1) if len(arr1) == len(arr2) else 2 * (len(arr1) > len(arr2)) - 1