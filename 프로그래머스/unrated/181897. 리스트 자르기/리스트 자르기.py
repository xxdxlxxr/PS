def solution(n, slicer, num_list):
    return [num_list[:slicer[1] + 1], num_list[slicer[0]:], num_list[slicer[0]:slicer[1] + 1], num_list[slicer[0]:slicer[1] + 1:slicer[2]]][n - 1]