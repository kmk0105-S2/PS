from collections import defaultdict

def solution(fees, records):
    total_hour = defaultdict(int)
    in_time = {}
    
    for line in records:
        time, num, flag = line.split()
        
        h, m = map(int, time.split(':'))
        current = h * 60 + m
        
        if flag == "IN":
            in_time[num] = current
            
        else:
            start = in_time.pop(num)
            total = current - start
            total_hour[num] += total
    
    # 아직 출차하지 않은 차량
    if len(in_time) != 0:
        current = 23 * 60 + 59
        
        for num, value in in_time.items():
            total = current - value
            total_hour[num] += total
    
    answer = []
    
    for num in sorted(total_hour):
        hour = total_hour[num]
        
        if hour <= fees[0]:
            money = fees[1]
        else:
            money = fees[1] + ((hour - fees[0] + fees[2] - 1) // fees[2]) * fees[3]
        
        answer.append(money)
    
    return answer