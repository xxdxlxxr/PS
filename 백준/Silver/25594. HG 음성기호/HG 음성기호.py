HG_symbol = {
    'a': 'aespa',
    'b': 'baekjoon',
    'c': 'cau',
    'd': 'debug',
    'e': 'edge',
    'f': 'firefox',
    'g': 'golang',
    'h': 'haegang',
    'i': 'iu',
    'j': 'java',
    'k': 'kotlin',
    'l': 'lol',
    'm': 'mips',
    'n': 'null',
    'o': 'os',
    'p': 'python',
    'q': 'query',
    'r': 'roka',
    's': 'solvedac',
    't': 'tod',
    'u': 'unix',
    'v': 'virus',
    'w': 'whale',
    'x': 'xcode',
    'y': 'yahoo',
    'z': 'zebra'
}

HG_length = {chr(i): len(HG_symbol[chr(i)]) for i in range(ord('a'), ord('z') + 1)}
S = input()
S_length = len(S)
HG_char_list, start, check = [], 0, True

while start < S_length:
    char = S[start]
    symbol = HG_symbol[char]
    length = HG_length[char]
    end = start + length
    part = S[start:end]

    if part != symbol:
        check = False
        break
    
    HG_char_list.append(char)
    start = end

if check:
    print('It\'s HG!')
    print(''.join(HG_char_list))
else:
    print('ERROR!')