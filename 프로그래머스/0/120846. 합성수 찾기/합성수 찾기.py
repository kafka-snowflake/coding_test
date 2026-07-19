def solution(n):
    # exclude prime numbers and 1
    def is_prime(n):
        if n < 2:
            return False
        for div in range(2, int(n**0.5)+1):
            if n % div == 0:
                return False
        return True
    return sum([
        1 for x in range(2,n+1)
        if not is_prime(x)
    ])