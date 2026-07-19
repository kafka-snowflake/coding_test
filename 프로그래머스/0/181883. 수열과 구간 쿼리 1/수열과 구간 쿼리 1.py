def solution(arr, queries):
    # def plus_one(l):
    #     return [x+1 for x in l]
    plus_ones = [0] * len(arr)
    for q in queries:
        for i in range(q[0],q[1]+1):
            plus_ones[i] += 1
    return [n+plus for n, plus in zip(arr, plus_ones)]
        
        