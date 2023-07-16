from math import prod

def solution(num_list):
    return sum(num_list) if len(num_list) > 10 else prod(num_list)