def solution(arr, queries):
    # from queries, we can make a list of increments.
    # if index 1 was included in queries 3 times, then 
    # arr[1] += 3
    # It is like a running sum.
    # Indicate with start(+1), end(-1) . Then all the indices
    # between get +1.
    # CASE: arr of length 4
    # If queries = [[0,2],[1,3]] 
    # => diff = [1,0,-1,0,0]->[1,1,0,-1,0]
    # increment -> [1,2,2,1]
    # so if arr=[1,1,1,1] => [2,3,3,1]
    n = len(arr)
    diff = [0] * (n+1)
    for s, e in queries:
        diff[s] += 1
        diff[e+1] -= 1
    increment=0
    
    # cumulatively 
    for i in range(n):
        increment+=diff[i]
        arr[i]+=increment
    return arr
        
        