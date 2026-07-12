def solution(id_list, report, k):
    reported = {i: [] for i in id_list} #신고당한 애들의 딕셔너리
    counted = {i: 0 for i in id_list}
    mail = {i: 0 for i in id_list}
    
    for p in set(report):
        user, user_reported = p.split()
        reported[user_reported].append(user)
        counted[user_reported] += 1
    
    for u in id_list:
        if counted[u] >= k:
            for reporter in reported[u]:
                mail[reporter] += 1
    
    return [mail[i] for i in id_list]
    