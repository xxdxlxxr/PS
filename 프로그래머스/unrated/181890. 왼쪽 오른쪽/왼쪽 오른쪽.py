def solution(str_list):
    l, r = 21,21
    
    if 'l' in str_list: l = str_list.index('l')
    if 'r' in str_list: r = str_list.index('r')
    
    return str_list[:l] if l < r else str_list[r + 1:] if r < 21 else []