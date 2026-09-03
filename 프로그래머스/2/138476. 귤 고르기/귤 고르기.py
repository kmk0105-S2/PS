from collections import defaultdict

def solution(k, tangerine):
    count = defaultdict(int)
    sm = 0
    answer = 0
    
    for key in tangerine:
        count[key] += 1 #1: 1, 2:2, 3:2, 4:1, 5:2
        
    sorted_count = sorted(count.items(), key=lambda x: x[1], reverse=True)
    
    for key, value in sorted_count:
        if sm >= k:
            break
        
        sm += value
        answer += 1
        
    return answer