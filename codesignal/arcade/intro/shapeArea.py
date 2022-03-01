# n = 1 - n = 1
# n = 2 - n = 5 (1 + 4)
# n = 3 - n = 13 (5 + 8)
# n = 4 - n = 25 (13 + 12)
# n = 5 - n = 41 (25 + 16) (being followed by 4)

def solution(n):
    var_fo, next_sum = 1, 4

    for i in range(1,n):
        var_fo += next_sum
        next_sum += 4

    return var_fo

# TOP SOLUTION
# def solution(n):
#     return n**2 + (n-1)**2

