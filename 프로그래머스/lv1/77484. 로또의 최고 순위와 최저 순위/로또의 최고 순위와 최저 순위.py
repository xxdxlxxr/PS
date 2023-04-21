def solution(lottos, win_nums):
    cnt = 0
    
    for number in lottos:
        if number in win_nums:
            cnt += 1
    
    return max(min(7 - cnt, 6) - lottos.count(0), 1), min(7 - cnt, 6)