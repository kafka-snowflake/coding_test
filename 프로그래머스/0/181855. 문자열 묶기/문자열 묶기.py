from collections import Counter
def solution(strArr):
    return max(Counter(map(lambda s: len(s), strArr)).values())