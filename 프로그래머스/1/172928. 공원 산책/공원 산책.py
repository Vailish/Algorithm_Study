def solution(park, routes):
    answer = []
    x, y = starting_point(park)
    for route in routes:
        r, c = x, y
        dir, val = route.split()
        val = int(val)
        
        if dir == "N":
            dr, dc = -1, 0
        elif dir == "S":
            dr, dc = 1, 0
        elif dir == "W":
            dr, dc = 0, -1
        else:
            dr, dc = 0, 1
        
        nr = r+dr
        nc = c+dc
        moving_point = 0
        is_error = False
        while moving_point < val:
            nr = r+dr
            nc = c+dc
            if 0 <= nr < len(park) and 0 <= nc < len(park[0]) and park[nr][nc] != "X":
                r, c = nr, nc
            else:
                is_error = True
                break
            moving_point += 1
        if not is_error:
            x, y = r, c
    answer = [x, y]
    return answer

def starting_point(park):
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == "S":
                return i, j
    return 0, 0