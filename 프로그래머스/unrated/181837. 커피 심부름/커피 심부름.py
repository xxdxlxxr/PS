def solution(order):
    return sum(4500 + ('cafelatte' in item) * 500 for item in order)