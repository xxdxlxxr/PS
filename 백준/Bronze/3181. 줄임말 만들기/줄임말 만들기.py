S = input().split()
print((S[0][0] + ''.join(word[0] for word in S[1:] if word not in ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili'])).upper())