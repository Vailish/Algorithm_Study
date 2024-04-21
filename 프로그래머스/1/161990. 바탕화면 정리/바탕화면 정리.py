def solution(wallpaper):
    answer = []
    # 제일 끝의 i좌표와 j좌표를 반환하면 됨
    # 최저 최저, 최고, 최고
    # [".#...",
    #  "..#..",
    #  "...#."]
    INF = 99999999
    min_r=INF
    min_c=INF
    max_r=0
    max_c=0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                min_r=min(min_r, i)
                min_c=min(min_c, j)
                max_r=max(max_r, i)
                max_c=max(max_c, j)
    answer.extend([min_r, min_c, max_r+1, max_c+1])
    return answer