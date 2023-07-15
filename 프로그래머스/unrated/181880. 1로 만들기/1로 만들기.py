def solution(num_list):
    return sum([len(bin(num)[2:]) - 1 for num in num_list])