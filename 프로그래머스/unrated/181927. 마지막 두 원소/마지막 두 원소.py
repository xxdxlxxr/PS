def solution(num_list):
    num_list.append(num_list[-1] - num_list[-2] if num_list[-2] < num_list[-1] else 2 * num_list[-1])
        
    return num_list