def solution(prices):
    stk = []
    answer = []
    
    for i in range(len(prices)):
        flag = False
        for j in range(i+1, len(prices)):
            if prices[i] > prices[j]:
                answer.append(j - i)
                flag = True
                break
            else:
                continue
                
        if not flag:
            answer.append(len(prices) - (i+1))
    
    return answer
                