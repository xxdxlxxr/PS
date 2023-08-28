def solution(order):
    return sum(4500 + ('caf' in item) * 500 for item in order)