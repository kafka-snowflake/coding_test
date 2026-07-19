def solution(n):
    answer = [n]
    while answer[-1] != 1:
        last_n = answer[-1]
        answer.append((last_n // 2) if last_n % 2 == 0 else (3*last_n + 1))
    return answer