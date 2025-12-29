def function(a, n):
    if n == 1:
        return
    
    for i in range(a + n // 3, a + 2 * (n // 3)):
        result[i] = ' '

    function(a, n // 3)
    function(a + n // 3 * 2, n // 3)

while 1:
    try:
        N = int(input())
        result = (3 ** N) * ['-']
        function(0, 3 ** N)
        print(''.join(result))
    except:
        break