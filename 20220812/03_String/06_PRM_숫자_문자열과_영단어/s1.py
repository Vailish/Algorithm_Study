def solution(s):
    answer = ''
    index = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7',
             'eight': '8', 'nine': '9'}
    for idx in index.keys():
        s = s.replace(idx, index.get(idx))
    answer = int(s)

    return answer
