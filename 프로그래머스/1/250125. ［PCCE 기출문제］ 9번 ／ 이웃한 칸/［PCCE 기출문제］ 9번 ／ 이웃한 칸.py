def solution(board, h, w):
    answer = 0
    
    for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        r = h+dr
        c = w+dc
        if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[h][w] == board[r][c]:
            answer += 1
    return answer