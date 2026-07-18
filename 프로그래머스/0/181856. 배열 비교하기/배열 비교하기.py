def solution(arr1, arr2):
    # 1  -> len(arr1)>len(arr2) or if len(arr1)==len(arr2) then sum(arr1)>sum(arr2)
    # 0  -> len(arr1)==len(arr2)
    # -1 -> len(arr1)<len(arr2) or if len(arr1)==len(arr2) then sum(arr1)<sum(arr2)
    # Compare length -> if equal length, then compare sum
    # When a problem says “compare X first, then compare Y if tied,” consider using (X, Y) as a tuple comparison.
    # CASE 1: [49, 13] <-> [70, 11, 2] 
    # (2,62) <-> (3,83) => -1
    # CASE 2: [100, 17, 84, 1] <-> [55, 12, 65, 36]
    # (4, 202) <-> (4, 168) => 1
    # CASE 3: [1,2,3,4,5] <-> [3,3,3,3,3]
    # (5,15) <-> (5,15) => 0
    
    x = (len(arr1), sum(arr1))
    y = (len(arr2), sum(arr2))
    return (x > y) - (x < y)
    
    