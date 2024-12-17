topic, pb = input(), False

for word in ['bigdata', 'public', 'society']:
    if word in topic:
        pb = True
        break

print('public bigdata' if pb else 'digital humanities')