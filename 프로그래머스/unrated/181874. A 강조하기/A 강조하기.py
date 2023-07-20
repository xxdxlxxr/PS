def solution(myString):
    return ''.join('A' if str == 'a' else str.lower() if str != 'A' and str.isupper() else str for str in myString)