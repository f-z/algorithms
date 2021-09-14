def solution(A):
    if not A or len(A) < 2:
        return 0

    sorted_list = sorted(A)

    cumsum = sorted_list[0] + sorted_list[1]
    i = 2

    while i < len(sorted_list):
        cumsum += cumsum + sorted_list[i]
        i += 1

    return cumsum