def solution(numbers):
    numbers.sort()
    return max(
        numbers[0] * numbers[1], # two smallest negatives
        numbers[-1] * numbers[-2] # two largest positives
    )