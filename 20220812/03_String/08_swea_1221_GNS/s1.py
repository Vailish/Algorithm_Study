# 1221. [S/W 문제해결 기본] 5일차 - GNS D3
# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14jJh6ACYCFAYD

# 숫자 리스트로 변경한 뒤, 정렬하고, 이를 다시 문자로 변환
# dic_words = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR" : 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
# dic_reverse = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
# for case in range(1, int(input())+1):
#     cs, len_words = input().split()
#     len_words = int(len_words)
#     words = list(input().split())
#     for idx in dic_words.keys():
#         words.replace(idx, dic_words.get(idx))
#     words.sort()
#     for idx in dic_words.values():
#         words.replace(idx, dic_reverse.get(idx))
#     print(words)

# 리스트로 받고, counts 정렬을 사용해서 새로 리스트를 만들어서 출력한다.

# 걍 다받자
for case in range(1, int(input())+1):
    cs, words_len = input().split()
    words_len = int(words_len)
    words = list(input().split())
    result = ''
    index = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    for idx in index:
        result += (idx + ' ') * words.count(idx)
    print(f'#{case} {result}')
