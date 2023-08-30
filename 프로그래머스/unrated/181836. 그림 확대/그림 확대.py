def solution(picture, k):
    answer = []
    
    for line in picture:
        answer += k * [''.join([k * pixel for pixel in line])]
    
    return answer