T, scores, answer = int(input()), list(map(int, input().split())), 0
scores += (5 - T) * [0]
answer += (400 * (scores[0] > scores[2]) + 108) * abs(scores[0] - scores[2]) + (93 * (scores[1] <= scores[3]) + 212) * abs(scores[1] - scores[3]) + 707 * scores[4]
print(4763 * answer)