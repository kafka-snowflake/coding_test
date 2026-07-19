def solution(my_string, s, e):
    """
    P   r   o   g   r   a   2   1   S   r   e   m   m   3 
    0   1   2   3   4   5   6   7   8   9  10  11  12  13
    """
    answer = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    # print(answer)
    return answer