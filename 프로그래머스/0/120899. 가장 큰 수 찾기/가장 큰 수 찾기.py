def solution(array):
    answer = max(array)
    index = array.index(answer)
    return [answer, index]