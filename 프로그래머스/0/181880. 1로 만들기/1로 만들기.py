def solution(num_list):
    # if n is odd, -1 and 0.5*n => ((n ^ 1) >> 1) => n >> 1
    # if n is even, 0.5*n       => (n >> 1)
    # 1     -> 0
    # 2-3   -> 1
    # 4-7   -> 2
    # 8-15  -> 3 (e.g. 9->4->2->1, 15->7->3->1)
    # for any n, next n is n >> 1
    return sum(n.bit_length() - 1 for n in num_list)