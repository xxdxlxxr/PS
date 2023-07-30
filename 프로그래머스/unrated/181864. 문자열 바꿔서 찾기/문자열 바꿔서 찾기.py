def solution(myString, pat):
    return int(pat in ''.join('A' if str == 'B' else 'B' for str in myString))