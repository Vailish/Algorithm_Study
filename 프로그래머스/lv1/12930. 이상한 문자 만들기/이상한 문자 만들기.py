def solution(s):
    chara = list(s.split(' '))
    result = []
    for chr in chara:
        tmp = ''
        for n in range(len(chr)):
            if not n % 2:  # 나머지가 1, 짝수번
                tmp += chr[n].upper()
            else:
                tmp += chr[n].lower()
        result.append(tmp)
    return ' '.join(result)
