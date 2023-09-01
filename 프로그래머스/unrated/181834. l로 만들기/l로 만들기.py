def solution(myString):
    return ''.join(chr(max(ord(str), ord('l'))) for str in myString)