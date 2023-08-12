def solution(ranks, attendance):
    return sum([sorted([[rank, i] for i, rank in enumerate(ranks) if attendance[i]])[:3][i][1] * 10 ** ((2 - i) * 2) for i in range(3)])