def solution(arr):
    
    def transform(x):
        if (x >= 50) and ((x & 1) == 0):
            return x // 2
        elif (x < 50) and ((x & 1) == 1):
            return x * 2
        else:
            return x
    return [transform(x) for x in arr]