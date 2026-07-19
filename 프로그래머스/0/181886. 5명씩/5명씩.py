def solution(names):
    answer = [name for idx, name in enumerate(names) if idx % 5 == 0 ]
    return answer