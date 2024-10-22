import sys
import re

for i in sys.stdin.readlines():
    while 1:
        result = re.sub('BUG', '', i)

        if 'BUG' in result:
            i = result
        else:
            print(result, end="")
            break