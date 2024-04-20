# data = code, date, maximum, remain 순
def solution(data, ext, val_ext, sort_by):
    answer = []
    # ext 인덱스 설정
    if ext == "code":
        idx=0
    elif ext == "date":
        idx=1
    elif ext == "maximum":
        idx=2
    else:
        idx=3
    
    if sort_by == "code":
        srt=0
    elif sort_by == "date":
        srt=1
    elif sort_by == "maximum":
        srt=2
    else:
        srt=3
    # ext 값이 val_ext 보다 작은 데이터만 뽑은 후
    for raw_data in data:
        if raw_data[idx] < val_ext:
            answer.append(raw_data)
    # sort_by기준 오름차순 정렬 후 반환
    return sorted(answer, key=lambda x: x[srt])