def solution(array, commands):
    arr = []
    answer = []
    for i in range(len(commands)):
        start = commands[i][0] - 1
        end = commands[i][1] - 1
        index = commands[i][2] - 1
        
        arr = array[start:end+1]
        arr.sort()
        answer.append(arr[index])
        
    return answer
            