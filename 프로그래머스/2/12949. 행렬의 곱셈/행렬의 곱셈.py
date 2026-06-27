def solution(arr1, arr2):
    n = len(arr1) #행
    m = len(arr1[0]) #열, n*m m*k = n*k
    k = len(arr2[0]) #arr2의 열
    answer = [[0] * k for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            for p in range(k):
                answer[i][p] += arr1[i][j] * arr2[j][p]
                
    return answer