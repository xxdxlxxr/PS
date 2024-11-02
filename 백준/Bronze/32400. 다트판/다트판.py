scores = list(map(int, input().split()))
twenty = scores.index(20)
Alice, Bob = (scores[twenty - 1] + scores[twenty] + scores[(twenty + 1) % 20]) / 3, sum(scores) / 20

print('Tie' if Alice == Bob else ['Alice', 'Bob'][Alice < Bob])