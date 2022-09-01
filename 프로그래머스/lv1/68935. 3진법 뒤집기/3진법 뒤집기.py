# def solution(n):
#     result = ''
    
#     while True:
#         a, b = divmod(n, 3)
#         n = a
#         result += b  # 어차피 뒤집으니까 그냥 뒤집어서 저장하자
#         if n < 3:
#             result += a
#             break
#     return int(result, 3)

def solution(n):
    rev_base = ''
    
    while n > 0:
        n, mod = divmod(n, 3)
        rev_base += str(mod)
        
    return int(rev_base, 3)