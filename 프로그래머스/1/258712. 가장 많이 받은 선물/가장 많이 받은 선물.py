from collections import defaultdict

def solution(friends, gifts):
    length = len(friends)
    name = defaultdict(str)
    store = [[0]*length for _ in range(length)]
    
    for i in range(length):
        name[friends[i]] = i
    
    for gift in gifts:
        key, value = gift.split()
        key = int(name[key]) #key가 value한테 선물 줌
        value = int(name[value])
        
        store[key][value] += 1
        
    gift_score = [0]*length
    
    for i in range(length):
        for j in range(length):
            gift_score[i] += store[i][j]
            gift_score[i] -= store[j][i]
        
    answer = [0] * length
    for key in range(length):
        for value in range(key+1, length):
            if store[key][value] > store[value][key]:
                answer[key] += 1
                
            elif store[key][value] < store[value][key]:
                answer[value] += 1
                
            else:
                if gift_score[key] > gift_score[value]:
                    answer[key] += 1
                
                elif gift_score[key] < gift_score[value]:
                    answer[value] += 1
                
        
    return max(answer)
    