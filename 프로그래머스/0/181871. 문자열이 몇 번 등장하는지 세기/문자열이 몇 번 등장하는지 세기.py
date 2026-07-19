def solution(myString, pat):
    return sum(
        myString.startswith(pat, i)
        for i in range(len(myString))
    )