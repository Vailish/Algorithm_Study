def solution(food):
    # 앞뒤가 똑같은 문자열 (팬린드롬) 생성
    foods = ""
    for i in range(1, len(food)):
        foods += str(i) * (food[i] // 2)
    return foods + "0" + foods[::-1]