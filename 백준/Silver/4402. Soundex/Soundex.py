import sys

for line in sys.stdin.read().split():
    soundex, before = '0', ''
    
    for char in line:
        if char == before:
            continue
        
        if char in 'BFPV' and soundex[-1] != '1':
            soundex += '1'
        elif char in 'CGJKQSXZ' and soundex[-1] != '2':
            soundex += '2'
        elif char in 'DT' and soundex[-1] != '3':
            soundex += '3'
        elif char == 'L' and soundex[-1] != '4':
            soundex += '4'
        elif char in 'MN' and soundex[-1] != '5':
            soundex += '5'
        elif char == 'R' and soundex[-1] != '6':
            soundex += '6'
        else:
            soundex += '0'
        
        before = char
        
    print(soundex.replace('0', ''))