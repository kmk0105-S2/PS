from collections import defaultdict

def solution(record):
    name = {}
    answer = []
    
    for line in record:
        parts = line.split()
        cmd = parts[0]
        uid = parts[1]
        if cmd != "Leave":       
            name[uid] = parts[2]
    
    for line in record:
        parts = line.split()
        cmd = parts[0]
        uid = parts[1]
        
        if cmd == "Enter":
            answer.append(f"{name[uid]}님이 들어왔습니다.")
        elif cmd == "Leave":
            answer.append(f"{name[uid]}님이 나갔습니다.")
        
    return answer