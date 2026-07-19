def solution(my_strings, parts):
    return "".join([
        my_strings[i][part[0]:part[1]+1]
        for i, part in enumerate(parts)
    ])