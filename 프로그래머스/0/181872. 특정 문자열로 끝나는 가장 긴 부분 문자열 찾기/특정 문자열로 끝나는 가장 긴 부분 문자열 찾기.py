def solution(myString, pat):
    answer = ''
    for i in range(len(myString)-len(pat),-1,-1):
        part = myString[i:i+len(pat)]
        if part == pat:
            answer = myString[0:i+len(pat)]
            break
    return answer