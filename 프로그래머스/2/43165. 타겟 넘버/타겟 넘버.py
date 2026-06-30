def solution(numbers, target):
    count = 0
    
    def dfs(index, answer):
        nonlocal count
        if index == len(numbers):       # 숫자 다 썼으면
            if answer == target:        # 최종 합이 타겟이면
                count += 1              # 경우의 수 +1
            return
        
        dfs(index + 1, answer + numbers[index])   # 이 숫자 +로
        dfs(index + 1, answer - numbers[index])   # 이 숫자 -로
    
    dfs(0, 0)
    return count