def solution(players, callings):
    answer, tmp = [], dict()
    
    for i, name in enumerate(players):
        tmp[name] = i
    
    for call in callings:
        before, after = tmp[call] - 1, tmp[call]
        tmp[players[before]], tmp[players[after]] = after, before
        players[before], players[after] = players[after], players[before]
    
    return players