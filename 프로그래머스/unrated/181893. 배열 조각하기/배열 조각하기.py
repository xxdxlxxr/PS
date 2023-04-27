def solution(arr, query):
    start, end = 0, 0
    
    for i in range(len(query)):
        if i % 2:
            start += query[i]
        else:
            end = start + query[i]
    
    return arr[start:end + 1]