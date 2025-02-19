import sys

translation = {'CU': 'see you',
               ':-)': "I’m happy",
               ':-(': "I’m unhappy",
               ';-)': 'wink',
               ':-P': 'stick out my tongue',
               '(~.~)': 'sleepy',
               'TA': 'totally awesome',
               'CCC': 'Canadian Computing Competition',
               'CUZ': 'because',
               'TY': 'thank-you',
               'YW': "you're welcome",
               'TTYL': 'talk to you later'}

for shortform in sys.stdin.readlines():
    shortform = shortform.strip()
    print(translation[shortform] if shortform in translation else shortform)