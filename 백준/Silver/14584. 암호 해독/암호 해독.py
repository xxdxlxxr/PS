secret, word_list = input(), [input() for _ in range(int(input()))]

for i in range(26):
    answer = ''

    for char in secret:
        ascii_code = ((ord(char) + i) % ord('z')) + 1
        
        if ascii_code < ord('a'):
            ascii_code += ord('a') - 1

        answer += chr(ascii_code)
    
    for word in word_list:

        if word in answer:
            print(answer)
            break