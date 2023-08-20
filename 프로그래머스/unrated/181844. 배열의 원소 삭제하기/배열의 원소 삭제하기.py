def solution(arr, delete_list):
    return [num for num in arr if not num in delete_list]