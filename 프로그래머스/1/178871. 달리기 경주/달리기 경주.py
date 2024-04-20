def solution(players, callings):
    answer = []
    # dictionary에 플레이어 : 등수로 생성
    result = {}
    rank = 0
    for player in players:
        result[player] = rank
        rank += 1
    # calling이 불릴때마다 해당 플레이어의 등수를 내리고 동일한 등수의 값의 녀석의 등수를 올린다
    for call in callings:
        idx = result[call]
        result[call] -= 1
        result[players[idx-1]] += 1
        players[idx], players[idx-1] = players[idx-1], players[idx]
    return players