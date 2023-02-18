def solution(cards1, cards2, goal):
    # 카드의 위치를 알려주는 포인트
    card1, card2 = 0, 0
    
    # goal를 for문을 돌리면서 card1과 card2에 있는지 확인
    # 있다면 진행, 없다면 No, 끝까지 진행되었다면 Yes
    
    for word in goal:
        if card1 < len(cards1) and word == cards1[card1]:
            card1 += 1
        elif card2 < len(cards2) and word == cards2[card2]:
            card2 += 1
        else:
            return "No"
    return "Yes"