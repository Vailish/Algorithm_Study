def solution(s):
    # 65 ~ 90 = A ~ Z
    # 97 ~ 122 = a ~ z
    chrs_lower = []
    chrs_upper = []
    for chr in s:
        if ord(chr) > 90:
            chrs_lower.append(chr)
        else:
            chrs_upper.append(chr)
    answer = sorted(chrs_lower)[::-1] + sorted(chrs_upper)[::-1]
    return ''.join(answer)