def solution(num_list):
    return sum(len(bin(num)) - 3 for num in num_list)