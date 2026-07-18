def solution(arr, n):
    is_arr_len_odd = int(len(arr) % 2 > 0)
    
    return [
        x + n if i % 2 == (1-is_arr_len_odd) else x 
        for i, x in enumerate(arr)
    ]