def solution(myString):
    return sorted(str for str in myString.split('x') if str)