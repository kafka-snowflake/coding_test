def solution(number):
    return sum(int(c) for c in str(number)) % 9