def solution(participant, completion):
    p = {i: 0 for i in participant}
    
    for name in participant:
        p[name] += 1
        
    for name in completion:
        p[name] -= 1
    
    for key in p:
        if p[key] == 1:
            return key
    
    