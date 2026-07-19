import re

def solution(myStr):
    # Split wherever one or more consecutive 'a', 'b', or 'c'
    # characters appear, then remove any empty strings.
    result = [
        part
        for part in re.split(r"[abc]+", myStr)
        if part
    ]

    # An empty list is falsy, so return ["EMPTY"] when no parts remain.
    return result or ["EMPTY"]