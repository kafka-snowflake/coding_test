from collections import Counter
def solution(s):
    counter_s = Counter(s.lower())
    return counter_s['p'] == counter_s['y']