def solution(arr, queries):
    for q in queries:
        x, y = q[0], q[1]
        arr[x], arr[y] = arr[y], arr[x]
    return arr