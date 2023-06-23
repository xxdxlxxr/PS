def solution(my_string):
    answer = 52 * [0]
    
    for string in my_string:
        answer[ord(string) - 65 - 6 * (string.islower())] += 1
    
    return answer