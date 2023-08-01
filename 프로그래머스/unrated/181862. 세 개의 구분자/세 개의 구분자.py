def solution(myStr):
    for char in 'abc':
        myStr = myStr.replace(char, ' ')
    
    return myStr.split() if len(myStr.split()) else ['EMPTY']