def solution(myString, pat):
    return int(''.join('A' if str == 'B' else 'B' for str in pat) in myString)